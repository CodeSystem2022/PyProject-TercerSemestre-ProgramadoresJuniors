import psycopg2
from .postgres import connect, disconnect
from .logging.logger_base import log


class TransactionNetwork:
    def __init__(self, network_type, description):
        self._id = None  # ID generado automáticamente por la base de datos
        self._network_type = network_type
        self._description = description
        self._banks = []

    def add_bank(self, bank):
        self._banks.append(bank)

    def save(self):
        try:
            conn = connect()
            cur = conn.cursor()

            if self._id is None:
                # Insertar una nueva red de transacciones y obtener el ID generado
                cur.execute(
                    "INSERT INTO transactions_networks (network_type, description) VALUES (%s, %s) RETURNING id",
                    (self._network_type, self._description),
                )
                self._id = cur.fetchone()[0]
            else:
                # Actualizar una red de transacciones existente
                cur.execute(
                    "UPDATE transactions_networks SET network_type = %s, description = %s WHERE id = %s",
                    (self._network_type, self._description, self._id),
                )

            # Eliminar todas las relaciones existentes de la red con los bancos
            cur.execute("DELETE FROM network_banks WHERE network_id = %s", (self._id,))

            # Insertar las nuevas relaciones entre la red y los bancos
            for bank in self._banks:
                cur.execute(
                    "INSERT INTO network_banks (network_id, bank_id) VALUES (%s, %s)",
                    (self._id, bank.id),
                )

            conn.commit()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)