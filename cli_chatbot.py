from chatbot import EnglishChatbot
from quiz_generator import generate_quiz
from chat_analysis import analyze_answer

if __name__ == "__main__":
    bot = EnglishChatbot()

    # Chat
    question = input("Ask something about English: ")
    answer = bot.respond(question)
    print("Bot:", answer)

    # Quiz
    quiz = generate_quiz("easy")
    print("\nHere's your quiz:")
    for item in quiz:
        print("Q:", item["question"])
        user_ans = input("Your answer: ")
        result = analyze_answer(user_ans, item["answer"])
        print(result["feedback"])