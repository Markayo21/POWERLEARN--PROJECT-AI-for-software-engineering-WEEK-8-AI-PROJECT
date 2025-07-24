# POWERLEARN--PROJECT-AI-for-software-engineering-WEEK-8-AI-PROJECT

# English Assistant Chatbot

A simple web-based English Assistant chatbot built using Flask and NLTK. The chatbot helps users find synonyms and responses to basic English language questions.

## Project Structure

english-assistant/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # Web interface (includes inbuilt CSS)
├── requirements.txt # Python dependencies
├── README.md # Project documentation (this file)

markdown
Copy
Edit

## Features

- User-friendly web interface with a clean, modern design.
- Synonym suggestion using NLTK WordNet.
- Graceful fallback responses for unsupported queries.
- Uses Flask to handle web interactions.

## Requirements

Install Python dependencies listed in `requirements.txt`:

Flask==2.3.2
nltk==3.8.1

perl
Copy
Edit

### Install the required Python libraries:

```bash
pip install -r requirements.txt
Also download NLTK corpora used for synonym generation:

python
Copy
Edit
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
How to Run
In your terminal or command prompt:

bash
Copy
Edit
python app.py
Then visit: http://127.0.0.1:5000 in your browser.

Sample Questions
You can try the following inputs:

What’s a synonym for happy?

Give a synonym for sad.

Can you help me?

I hate you.

Example Response:
vbnet
Copy
Edit
You: What's a synonym for happy?
Assistant: A synonym for 'happy' is 'contented'
For unsupported or unrelated input, the assistant responds:

rust
Copy
Edit
I'm still learning. Can you ask something else?
File: index.html
This is the front-end of the chatbot with inbuilt CSS:

html
Copy
Edit
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>English Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f6fc;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            align-items: center;
            justify-content: center;
        }

        .container {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            width: 90%;
            max-width: 500px;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
        }

        form {
            display: flex;
            margin-top: 1rem;
        }

        input[type="text"] {
            flex: 1;
            padding: 0.8rem;
            font-size: 1rem;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        input[type="submit"] {
            padding: 0.8rem 1rem;
            margin-left: 0.5rem;
            font-size: 1rem;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .response {
            margin-top: 1.5rem;
            background: #ecf0f1;
            padding: 1rem;
            border-radius: 10px;
            min-height: 60px;
        }

        .label {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>English Assistant</h1>
        <form method="post">
            <input type="text" name="user_input" placeholder="Type your question..." required>
            <input type="submit" value="Ask">
        </form>
        {% if user_input %}
        <div class="response">
            <p><span class="label">You:</span> {{ user_input }}</p>
            <p><span class="label">Assistant:</span> {{ response }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
Author
Mark Wainaina Iraya



