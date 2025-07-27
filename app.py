from flask import Flask, request, render_template
from nltk.corpus import wordnet
import nltk
from model import db

app = Flask(__name__)

# Setup database config - using SQLite here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english_tutor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind the database to this app
db.init_app(app)

# Ensure required NLTK resources are available
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if "synonym for" in user_input.lower():
            keyword = user_input.lower().split("synonym for")[-1].strip().rstrip("?")
            synonyms = get_synonyms(keyword)
            if synonyms:
                response = f"Some synonyms for '{keyword}' are: {', '.join(synonyms[:5])}."
            else:
                response = f"Sorry, I couldn’t find synonyms for '{keyword}'."
        else:
            response = "I'm still learning. Can you ask something like: 'What's a synonym for happy?'"
    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)

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



