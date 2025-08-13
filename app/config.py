from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    jwt_secret_key = os.getenv('jwt_key')
    sql = os.getenv('sql_url')