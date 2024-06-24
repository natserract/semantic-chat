import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_KEY = os.environ.get('OPENAI_KEY')
    OPENAI_MODEL = os.environ.get('OPENAI_MODEL')
    DB_NAME = os.environ.get('DB_NAME')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
