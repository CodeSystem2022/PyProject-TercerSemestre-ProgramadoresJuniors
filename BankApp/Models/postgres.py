import psycopg2

def connect():
    try:
        conn =psycopg2.connect(
                database="BankApp",
                user="postgres",
                password="xxxxx",
                host="127.0.0.1",
                port="5432",
            )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error al conectarse a la base de datos:", error)

def disconnect(conn):
    if conn:
        conn.close()