import psycopg2
from .postgres import connect, disconnect
from .logging.logger_base import log


class Client:
    def __init__(self, name, address, phone, bank_id):
        self._id = None  # ID generado automáticamente por la base de datos
        self._name = name
        self._address = address
        self._phone = phone
        self._bank_id = bank_id

    def save(self):
        try:
            conn = connect()
            cur = conn.cursor()

            if self._id is None:
                # Insertar un nuevo cliente y obtener el ID generado
                cur.execute(
                    "INSERT INTO clients (name, address, phone, bank_id) VALUES (%s, %s, %s, %s) RETURNING id",
                    (self._name, self._address, self._phone, self._bank_id),
                )

                # print(cur.fetchone()[0])
                self._id = cur.fetchone()[0]
            else:
                # Actualizar un cliente existente
                cur.execute(
                    "UPDATE clients SET name = %s, address = %s, phone = %s, bank_id = %s WHERE id = %s",
                    (self._name, self._address, self._phone, self._bank_id, self._id),
                )

            conn.commit()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

    @staticmethod
    def get_by_id(client_id):
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM clients WHERE id = %s", (client_id,))
            row = cur.fetchone()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        if row:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client._id = client_id
            return client

        return None

    @staticmethod
    def get_all():
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM clients")
            rows = cur.fetchall()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        clients = []
        for row in rows:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client._id = client_id
            clients.append(client)

        return clients

    @staticmethod
    def get_by_address_name(address, name):
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute(
                "SELECT * FROM clients WHERE address = %s AND name = %s",
                (address, name),
            )
            row = cur.fetchone()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        if row:
            client_id, name, address, phone, bank_id = row
            client = Client(name, address, phone, bank_id)
            client._id = client_id
            return client

        return None
