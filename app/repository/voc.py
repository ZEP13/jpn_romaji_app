from app.db_connection import conn
from psycopg import sql, OperationalError
from typing import List, Tuple, Optional


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
                            nb_good_asw INT DEFAULT 0,
                            nb_attempts INT DEFAULT 0
                        )
                    """)
                )
    except OperationalError as e:
        print("Could not create the db voc:", e)


def find_trad_fr_jpn(fr_meaning: str) -> List[Tuple[str, str]]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT  fr_meaning, jpn_meaning  FROM jpn_romaji.voc WHERE fr_meaning LIKE %s",
                    (f"%{fr_meaning}%",)
                )
                rows = cur.fetchall()
                return rows
    except OperationalError as e:
        print(f"Could not find word for '{fr_meaning}': {e}")
        return []


def find_trad_jpn_fr(jpn_meaning: str) -> List[Tuple[str, str]]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT fr_meaning, jpn_meaning FROM jpn_romaji.voc WHERE jpn_meaning LIKE %s",
                    (f"%{jpn_meaning}%",)
                )
                rows = cur.fetchall()
                return rows
    except OperationalError as e:
        print(f"Could not find word for '{jpn_meaning}': {e}")
        return []


def add_vocabulary(jpn_meaning: str, fr_meaning: str) -> None:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO jpn_romaji.voc (jpn_meaning, fr_meaning) VALUES (%s,%s)",
                    (jpn_meaning, fr_meaning)
                )
    except OperationalError as e:
        print("could not add new voc", e)


def get_number_of_rand_voc(number: int) -> List[Tuple[int, str, str, int, int]]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    sql.SQL(
                        "SELECT id, fr_meaning, jpn_meaning, nb_good_asw, nb_attempts FROM jpn_romaji.voc ORDER BY RANDOM() LIMIT %s"),
                    (number,)
                )
                rows = cur.fetchall()
                return rows
    except OperationalError as e:
        print("Could not fetch random voc:", e)
        return []


def update_voc_stats(id_word: int, nb_good_asw: int, nb_attempts: int) -> None:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "UPDATE jpn_romaji.voc SET nb_good_asw = %s, nb_attempts = %s WHERE id  = %s",
                    (nb_good_asw, nb_attempts, id_word)
                )
    except OperationalError as e:
        print("Could not update voc stats:", e)


def get_last_added() -> Optional[Tuple[str, str]]:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "SELECT jpn_meaning, fr_meaning FROM jpn_romaji.voc ORDER BY id DESC LIMIT 1"
                )
                rows = cur.fetchone()
                return rows
    except OperationalError as e:
        print("Could not fetch last added voc:", e)
        return None


def delete_vocabulary(jpn_meaning: str, fr_meaning: str) -> None:
    try:
        with conn.get_db_connection() as connection:
            with connection.cursor() as cur:
                cur.execute(
                    "DELETE FROM jpn_romaji.voc WHERE jpn_meaning = %s AND fr_meaning = %s",
                    (jpn_meaning, fr_meaning)
                )
                connection.commit()
    except OperationalError as e:
        print("Could not delete voc:", e)
