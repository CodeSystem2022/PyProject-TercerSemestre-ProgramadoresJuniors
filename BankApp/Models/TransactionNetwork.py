import psycopg2
from .postgres import connect, disconnect

class TransactionNetwork:
    def __init__(self, network_type, description):
        self.id = None  # ID generado automáticamente por la base de datos
        self.network_type = network_type
        self.description = description
        self.banks = []

    def add_bank(self, bank):
        self.banks.append(bank)

    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar una nueva red de transacciones y obtener el ID generado
            cur.execute(
                "INSERT INTO transactions_networks (network_type, description) VALUES (%s, %s) RETURNING id",
                (self.network_type, self.description),
            )
            self.id = cur.fetchone()[0]
        else:
            # Actualizar una red de transacciones existente
            cur.execute(
                "UPDATE transactions_networks SET network_type = %s, description = %s WHERE id = %s",
                (self.network_type, self.description, self.id),
            )

        # Eliminar todas las relaciones existentes de la red con los bancos
        cur.execute(
            "DELETE FROM network_banks WHERE network_id = %s", (self.id,)
        )

        # Insertar las nuevas relaciones entre la red y los bancos
        for bank in self.banks:
            cur.execute(
                "INSERT INTO network_banks (network_id, bank_id) VALUES (%s, %s)",
                (self.id, bank.id),
            )

        conn.commit()
        disconnect(conn)