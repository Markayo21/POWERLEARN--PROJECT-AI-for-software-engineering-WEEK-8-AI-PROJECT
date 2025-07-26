def analyze_answer(user_answer, correct_answer):
    user = user_answer.strip().lower()
    correct = correct_answer.strip().lower()
    score = 1 if user == correct else 0
    feedback = "✅ Correct!" if score else f"❌ Incorrect. Correct answer: {correct_answer}"
    return {"score": score, "feedback": feedback}

if __name__ == "__main__":
    ua = input("Your Answer: ")
    ca = "walks"
    result = analyze_answer(ua, ca)
    print("Feedback:", result["feedback"])
    print("Score:", result["score"])
