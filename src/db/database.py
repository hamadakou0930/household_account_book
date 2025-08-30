import psycopg2
from psycopg2 import sql

DATABASE_CONFIG = {
    'dbname': 'household_account_book',
    'user': 'user',
    #'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

def create_table():
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id SERIAL PRIMARY KEY,
                    date DATE NOT NULL,
                    category VARCHAR(50) NOT NULL,
                    amount INTEGER NOT NULL,
                    memo TEXT
                )
            """)
            conn.commit()

def insert_record(date, category, amount, memo=""):
    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO records (date, category, amount, memo)
                VALUES (%s, %s, %s, %s)
            """, (date, category, amount, memo))
            conn.commit()