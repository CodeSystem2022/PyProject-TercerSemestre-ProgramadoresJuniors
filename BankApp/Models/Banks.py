from .postgres import connect, disconnect
from .logging.logger_base import log


class Bank:
    def __init__(self, name, network_type_id):
        self._id = None  # ID generado automáticamente por la base de datos
        self._name = name
        self._network_type_id = network_type_id

        # Guardar la instancia automáticamente
        # self.save()

    def save(self):
        try:
            conn = connect()
            cur = conn.cursor()

            if self._id is None:
                # Insertar un nuevo banco y obtener el ID generado
                cur.execute(
                    "INSERT INTO banks (name, network_type_id) VALUES (%s, %s) RETURNING id",
                    (self._name, self._network_type_id),
                )
                self._id = cur.fetchone()[0]
            else:
                # Actualizar un banco existente
                cur.execute(
                    "UPDATE banks SET name = %s WHERE id = %s", (self._name, self._id)
                )
            conn.commit()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

    @staticmethod
    def get_all():
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM banks")
            rows = cur.fetchall()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        banks = []
        # print(rows)
        for row in rows:
            bank_id, name, network = row
            bank = Bank(name, network)
            bank._id = bank_id
            banks.append(bank)

        return banks

    @staticmethod
    def get_by_id(bank_id):
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM banks WHERE id = %s", (bank_id,))
            row = cur.fetchone()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        if row:
            bank_id, name, network_type_id = row
            bank = Bank(name, network_type_id)
            bank._id = bank_id
            return bank

        return None