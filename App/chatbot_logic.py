from nltk.corpus import wordnet
import nltk

# Ensure data is available
nltk.download("wordnet")
nltk.download("omw-1.4")

def get_response(message):
    message = message.lower()

    if "synonym for" in message:
        word = message.replace("synonym for", "").strip()
        synonyms = wordnet.synsets(word)
        if synonyms:
            synonym_words = set()
            for syn in synonyms:
                for lemma in syn.lemmas():
                    synonym_words.add(lemma.name())
            return f"Some synonyms for '{word}' are: {', '.join(list(synonym_words)[:5])}."
        else:
            return f"Sorry, I couldn't find synonyms for '{word}'."

    elif "hello" in message:
        return "Hello! How can I help you today?"

    else:
        return "I'm still learning. Can you ask something else?"




