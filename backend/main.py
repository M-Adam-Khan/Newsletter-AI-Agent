from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

from newsletter_ai.graph_builder import build_graph
from newsletter_ai.utils import save_newsletter_to_word
from backend.schema import NewsletterRequest, NewsletterResponse

app = FastAPI()

# CORS Middleware - allow all origins for development, customize for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve your frontend static files (index.html, CSS, JS, etc.) from "frontend" folder
app.mount("/static", StaticFiles(directory="frontend", html=True), name="frontend")

# Redirect root URL "/" to your frontend index.html automatically
@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/static/index.html")

# Build LangGraph app once on startup
langgraph_app = build_graph()

@app.post("/generate", response_model=NewsletterResponse)
def generate_newsletter(request: NewsletterRequest):
    try:
        state = langgraph_app.invoke({"topic": request.topic})
        newsletter_text = state.get("newsletter", "")

        save_dir = "Generated Newsletters"
        os.makedirs(save_dir, exist_ok=True)
        filename = f"{request.topic}_newsletter.docx"
        file_path = os.path.join(save_dir, filename)

        save_newsletter_to_word(newsletter_text, filename=file_path)

        return NewsletterResponse(newsletter=newsletter_text, filename=filename)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{filename}")
async def download_newsletter(filename: str):
    folder = "Generated Newsletters"
    file_path = os.path.join(folder, filename)

    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    else:
        raise HTTPException(status_code=404, detail="File not found.")
