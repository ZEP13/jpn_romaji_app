import os
import psycopg
from psycopg import OperationalError
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    try:
        return psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise
