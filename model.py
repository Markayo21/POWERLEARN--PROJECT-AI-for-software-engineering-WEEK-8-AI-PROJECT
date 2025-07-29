from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Initialize sqlalchemy object

db = SQLAlchemy()

# Create user model to store users who register
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(200), nullable=False)  
    email = db.Column(db.String(200), nullable=False, unique=True)  
    password = db.Column(db.String(200), nullable=False)  


# Create Chat sessions model to store chat sessions
class ChatSession(db.Model):
    __tablename__ = 'chat_sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    messages = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='sessions')
 


