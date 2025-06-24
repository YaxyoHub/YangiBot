import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DATABASE_NAME')
db_user = os.getenv('DATABASE_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_port = os.getenv('DATABASE_PORT')


def connect_psql():
    """
    connect to postgres database
    """
    DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

    return psycopg2.connect(DATABASE_URL)

"""Userlarni ko'rish"""
def get_user():
    connect = connect_psql()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users;')
    datas = cursor.fetchall()
    cursor.close()
    connect.close()
    return datas

def add_user(full_name: str, tg_id: int):
    connect = connect_psql()
    cursor = connect.cursor()
    cursor.execute("SELECT tg_id FROM users WHERE tg_id = %s", (tg_id,))
    result = cursor.fetchone()
    if not result:
        cursor.execute("INSERT INTO users (name, tg_id) VALUES (%s, %s)", (full_name, tg_id))
        connect.commit()
    connect.close()

def get_admin():
    connect = connect_psql()
    cursor = connect.cursor()
    cursor.execute("SELECT tg_id FROM admins;")
    datas = cursor.fetchall()
    cursor.close()
    connect.close()
    return datas


