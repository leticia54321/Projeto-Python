import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()



# Conectar no banco
def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

print("Conexão bem-sucedida!")


def close_connection(conn):
    if conn:
        conn.close()
