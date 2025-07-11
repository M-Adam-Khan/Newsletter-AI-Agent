# AI Powered Newsletter Generator

A powerful and intelligent newsletter generator that **researches**, **writes**, **proofreads**, and **delivers** high-quality newsletters using state-of-the-art LLMs.

Built with **LangGraph**, **FastAPI**, and a modern **HTML/CSS/JS frontend**, this project is ideal for professionals, marketers, educators, and enthusiasts looking to create content in seconds.

---

## ✨ Features

- Enter a topic and get a full newsletter in seconds  
- Automatically researches latest trends, innovations, risks, and applications  
- Converts raw research into a professionally structured newsletter  
- Utilizes **GROQ LLaMA 3** via **LangChain & LangGraph**  
- Exports output as a **.docx Word document**  
- Beautiful and responsive **frontend interface**  
- Powered by **FastAPI backend**  
- Clean, modular, and production-ready code structure  

---

## 🛠️ Tech Stack

| Layer         | Technologies Used                            |
|---------------|-----------------------------------------------|
| **LLM**        | GROQ LLaMA 3 (8B) via `langchain_groq`        |
| **Workflow**   | LangGraph (`StateGraph`)                     |
| **Backend**    | FastAPI, Pydantic, Uvicorn                   |
| **Frontend**   | HTML5, CSS3, JavaScript                      |
| **Export**     | `python-docx` for Word document generation   |
| **Utilities**  | dotenv, CORS middleware                      |

---

## 🚀 Getting Started

### 0. Add API Key
Create a `.env` file in the root folder and paste your [GROQ](https://console.groq.com/) API key:

```env
GROQ_API_KEY=your_groq_api_key

1. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. Run the Backend
bash
Copy
Edit
uvicorn backend.main:app --reload
3. Open Frontend
Visit your browser at:

arduino
Copy
Edit
http://127.0.0.1:8000/static/index.html
📡 API Endpoints
Method	Endpoint	Description
POST	/generate	Generates newsletter from user topic
GET	/download/{file}	Downloads the generated .docx file
GET	/	Root health check

🧪 Example
Input Topic
nginx
Copy
Edit
AI in Healthcare
Output Sections
Trending Technologies

Innovations in the Field

Risks and Challenges

Real-World Applications

Conclusion

Further Reading / Sources

👨‍💻 Author
Muhammad Adam Khan