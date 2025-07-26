from transformers import pipeline

class EnglishChatbot:
    def __init__(self):
        # Load the QA model
        self.qa_pipeline = pipeline(
            "question-answering",
            model="distilbert-base-uncased-distilled-squad"
        )

    def respond(self, question, context="A noun is a word used to identify any of a class of people, places, or things."):
        try:
            result = self.qa_pipeline(question=question, context=context)
            return result["answer"]
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    bot = EnglishChatbot()
    question = "What is a noun?"
    print("Question:", question)
    print("Answer:", bot.respond(question))
