import os
import psycopg
from psycopg import OperationalError


def get_db_connection():
    try:
        return psycopg.connect(
            dbname=os.getenv("DB_NAME", "postgres"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", 5432),
        )
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise
