from newsletter_ai.graph_builder import build_graph
from newsletter_ai.utils import save_newsletter_to_word

if __name__ == "__main__":
    app = build_graph()

    user_topic = input("Enter newsletter topic: ")
    final_state = app.invoke({"topic": user_topic})

    newsletter_text = final_state.get("newsletter", "")
    print("\n📨 Final Newsletter Output:\n")
    print(newsletter_text)

    save_newsletter_to_word(newsletter_text, filename=f"{user_topic}_newsletter.docx")
