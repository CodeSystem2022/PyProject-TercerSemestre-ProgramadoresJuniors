import psycopg2
import os
from dotenv import load_dotenv
from .logging.logger_base import log

load_dotenv()


def connect():
    try:
        conn = psycopg2.connect(
            database="BankApp",
            user="postgres",
            password=os.getenv("PASSWORD_DB"),
            host="127.0.0.1",
            port="5432",
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        log.error("Error al conectarse a la base de datos: ", error)


def disconnect(conn):
    if conn:
        conn.close()
