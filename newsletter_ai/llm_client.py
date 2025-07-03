from langchain_groq import ChatGroq
from newsletter_ai.config import GROQ_API_KEY

llm = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)