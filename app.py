from flask import Flask, request, render_template, redirect, url_for, session, flash
from nltk.corpus import wordnet
from werkzeug.security import  check_password_hash, generate_password_hash
from model import db, User, ChatSession
import nltk


app = Flask(__name__)

# Setup database config - using SQLite here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english_tutor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key for session management
app.secret_key = "your-temporary-secret-key"  # Replace later


# Bind the database to this app
db.init_app(app)

# Ensure required NLTK resources are available
nltk.download('wordnet')
nltk.download('omw-1.4')

@app.route("/")
def index():
    return redirect(url_for("login"))


# Register route
@app.route("/register", methods=["GET", "POST"])    
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("⛔Email already registered.", "danger")
            return redirect(url_for("register"))

       # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

         # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash("✅Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")  

# Login route
@app.route("/login", methods=["GET", "POST"])   
#Define the login route
def login():
    if request.method == "POST":
        #Get the form data
        username  = request.form["username"]
        password = request.form["password"]
        
        #Query user from database by name
        user =User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            #Login usccess and store user in session
            session["user_id"] = user.id
            flash("✅Login successful!", "success")
            return redirect(url_for("chatbot"))  # Redirect to chatbot route
            
        else:
            flash("⛔Invalid username or password.", "danger")
            return redirect(url_for("login"))
        
    # If GET request, render the login page
    return render_template("login.html")


# logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("✅You have been logged out.", "success")
    return redirect(url_for('login'))

# home route
@app.route('/home')
def home():
    if "user_id" in session:
        return render_template("home.html", user=session["user_id"])
    else:
        flash("Please login first", "warning")
        return redirect(url_for("login"))
    
   
# Dashboard route
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("⚠️ Login required.", "warning")
        return redirect(url_for("login"))
    return render_template("dashboard.html")


# Function to get synonyms using WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)

# Chatbot route
@app.route("/chatbot", methods=["GET", "POST"]) #--- Mark i edited here to avoid dashboard route conflict
def chatbot():
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





