from langchain_core.prompts import ChatPromptTemplate
from newsletter_ai.llm_client import llm
from newsletter_ai.schema import AppState

def research_node(state: AppState) -> AppState:
    topic = state["topic"]
    prompt = ChatPromptTemplate.from_template(
        """
        Research and summarize the latest developments in the topic: {topic}.
        Please organize the output into these sections with headers:

        1. Trending Technologies  
        2. Innovations in the Field  
        3. Risks and Challenges  
        4. Real-World Applications

        Provide concise bullet points or short paragraphs under each section.
        """
    )
    chain = prompt | llm
    result = chain.invoke({"topic": topic})
    return {"topic": topic, "research": result.content}

def formatting_node(state: AppState) -> AppState:
    prompt = ChatPromptTemplate.from_template(
        """
        You are a professional newsletter writer. Turn the following research into an engaging, clear, and informative newsletter.

        Make sure to:

        - Use short paragraphs and clear headers  
        - Explain why the points are important or impactful  
        - Keep a professional, friendly tone  
        - Include a short conclusion summarizing the key takeaways  
        - Add a call to action encouraging readers to stay updated or share the newsletter
        - Optionally add a "Further Reading" or "Sources" section with links or references.

        Research Content:
        {research}
        """
    )
    chain = prompt | llm
    result = chain.invoke({"research": state["research"]})
    return {"topic": state["topic"], "research": state["research"], "newsletter": result.content}

def display_node(state: AppState) -> AppState:
    print("\n Final Newsletter Output:\n")
    print(state["newsletter"])
    return state
