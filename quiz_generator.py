import random
import json

def generate_quiz(level="easy"):
    quiz_bank = {
        "easy": [
            {"question": "Choose the correct verb form: 'He ___ every day.'", "answer": "walks"},
            {"question": "What is the plural of 'child'?", "answer": "children"},
            {"question": "Identify the noun: 'The cat sat on the mat.'", "answer": "cat"}
        ],
        "medium": [
            {"question": "Choose the correct form: 'They ___ been to Paris.'", "answer": "have"},
            {"question": "What part of speech is 'quickly'?", "answer": "adverb"},
            {"question": "Form a question using: 'you / go / yesterday'", "answer": "Did you go yesterday?"}
        ]
    }
    quiz = random.sample(quiz_bank.get(level, quiz_bank["easy"]), 3)
    with open("quizzes.json", "w") as f:
        json.dump(quiz, f, indent=2)
    return quiz

if __name__ == "__main__":
    qz = generate_quiz("easy")
    print("Generated Quiz:")
    for item in qz:
        print("Q:", item["question"], "| A:", item["answer"])