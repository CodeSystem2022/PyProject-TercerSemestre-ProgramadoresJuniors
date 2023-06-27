import psycopg2
from .postgres import connect, disconnect

class Bank:
    def __init__(self, name):
        self.id = None  # ID generado automáticamente por la base de datos
        self.name = name

        # Guardar la instancia automáticamente
        self.save()

    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar un nuevo banco y obtener el ID generado
            cur.execute("INSERT INTO banks (name) VALUES (%s) RETURNING id", (self.name,))
            self.id = cur.fetchone()[0]
        else:
            # Actualizar un banco existente
            cur.execute("UPDATE banks SET name = %s WHERE id = %s", (self.name, self.id))

        conn.commit()
        disconnect(conn)

    @staticmethod
    def get_all():
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM banks")
        rows = cur.fetchall()
        disconnect(conn)

        banks = []
        for row in rows:
            bank_id, name = row
            bank = Bank(name)
            bank.id = bank_id
            banks.append(bank)

        return banks