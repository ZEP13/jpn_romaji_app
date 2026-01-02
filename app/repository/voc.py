import psycopg
import db_connection.conn as conn
from psycopg import sql, OperationalError


def create_voc_table():
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    sql.SQL("""
                        CREATE TABLE IF NOT EXISTS voc (
                            id SERIAL PRIMARY KEY,
                            fr_meaning TEXT NOT NULL,
                            jpn_meaning TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                )
    except OperationalError as e:
        print("Could not create the db voc:", e)


def find_trad_fr_jpn(fr_meaning: str) -> list[str]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM voc WHERE fr_meaning LIKE %s",
                    (f"%{fr_meaning}%",)
                )
                rows = cur.fetchall()
                return [row[0] for row in rows]
    except OperationalError as e:
        print(f"Could not find word or trad with meaning '{fr_meaning}': {e}")
        return []


def find_trad_jpn_fr(jpn_meaning: str) -> list[str]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT * FROM voc WHERE fr_meaning LIKE %s",
                    (f"%{jpn_meaning}%",)
                )
                rows = cur.fetchall()
                return [row[1] for row in rows]
    except OperationalError as e:
        print(f"Could not find word or trad with meaning '{jpn_meaning}': {e}")
        return []


def add_vocabulary(jpn_meaning: str, fr_meaning: str) -> None:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO voc (jpn_meaning, fr_meaning) VALUES (%s,%s)",
                    (jpn_meaning, fr_meaning)
                )
    except OperationalError as e:
        print("could not add new voc", e)
