import os
from newsletter_ai.graph_builder import build_graph
from newsletter_ai.utils import save_newsletter_to_word

if __name__ == "__main__":
    app = build_graph()

    user_topic = input("Enter newsletter topic: ")
    final_state = app.invoke({"topic": user_topic})

    newsletter_text = final_state.get("newsletter", "")
    print("\n Final Newsletter Output:\n")
    print(newsletter_text)

    # Ensure the folder exists
    output_folder = "Generated Newsletters"
    os.makedirs(output_folder, exist_ok=True)

    # Create the full file path inside the folder
    filename = os.path.join(output_folder, f"{user_topic}_newsletter.docx")

    save_newsletter_to_word(newsletter_text, filename=filename)