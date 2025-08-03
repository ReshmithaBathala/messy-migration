import os
from dotenv import load_dotenv

load_dotenv()

FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
DATABASE = os.getenv("DATABASE", "users.db")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
