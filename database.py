from app.app import create_app
from app import db
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Print the environment variables for debugging
print("Environment Variables Loaded:")
print("FLASK_APP:", os.getenv('FLASK_APP'))
print("FLASK_ENV:", os.getenv('FLASK_ENV'))
print("SQLALCHEMY_DATABASE_URI:", os.getenv('SQLALCHEMY_DATABASE_URI'))
print("DEV_DATABASE_URI:", os.getenv('DEV_DATABASE_URI'))

def create_db():
    try:
        # Create the Flask application instance
        app = create_app()

        # Check for the site database file and remove it if it exists
        # Remove the logic that deletes the existing database file

        
        with app.app_context():
            db.create_all()

        logging.info("Database created successfully.")
    except Exception as e:
        logging.error(f"Failed to create database: {e}")

if __name__ == '__main__':
    create_db()  # Commenting out the database creation for production
