import psycopg2
from .postgres import connect, disconnect


class Client:
    def __init__(self, name, address, phone, bank_id):
        self.id = None  # ID generado automáticamente por la base de datos
        self.name = name
        self.address = address
        self.phone = phone
        self.bank_id = bank_id

    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar un nuevo cliente y obtener el ID generado
            cur.execute(
                "INSERT INTO clients (name, address, phone, bank_id) VALUES (%s, %s, %s, %s) RETURNING id",
                (self.name, self.address, self.phone, self.bank_id),
            )
            
            #print(cur.fetchone()[0])
            self.id = cur.fetchone()[0]
        else:
            # Actualizar un cliente existente
            cur.execute(
                "UPDATE clients SET name = %s, address = %s, phone = %s, bank_id = %s WHERE id = %s",
                (self.name, self.address, self.phone, self.bank_id, self.id),
            )

        conn.commit()
        disconnect(conn)

    @staticmethod
    def get_by_id(client_id):
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM clients WHERE id = %s", (client_id,))
        row = cur.fetchone()

        disconnect(conn)

        if row:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client.id = client_id
            return client

        return None
    
    
    @staticmethod
    def get_all():
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM clients")
        rows = cur.fetchall()

        disconnect(conn)

        clients = []
        for row in rows:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client.id = client_id
            clients.append(client)

        return clients


    @staticmethod
    def get_by_address_name(address, name):
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM clients WHERE address = %s AND name = %s", (address, name))
        row = cur.fetchone()

        disconnect(conn)

        if row:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client.id = client_id
            return client

        return None



