from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User, ChatSession

# Define user registrtion function
def user_registration(name, email, password):
    # Check if user already exist
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return False, "⛔User already exists."
    #Hash the password
    hashed_password = generate_password_hash(password)

    # Create new user
    new_user = User(name=name, email=email, password= hashed_password)

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return True, "✅You have registered successfully."