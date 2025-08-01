# create_tables.py
from db_setup import db, app

with app.app_context():
    db.create_all()
    print("Tables created successfully.")