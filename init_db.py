# init_db.py
from app import app
from model import db

with app.app_context():
    db.create_all()
    print("✅ Database created.")
