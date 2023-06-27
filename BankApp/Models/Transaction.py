from datetime import datetime
import psycopg2
from .postgres import connect, disconnect


class Transaction:
    def __init__(self, client_id, account_id, transaction_network_id, bank_id, amount, transaction_type):
        self.id = None  # ID generado automáticamente por la base de datos
        self.client_id = client_id
        self.account_id = account_id
        self.transaction_network_id = transaction_network_id
        self.bank_id = bank_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now()

    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar una nueva transacción y obtener el ID generado
            cur.execute(
                "INSERT INTO transactions (client_id, account_id, transactions_network_id, bank_id, amount, date, type) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
                (self.client_id, self.account_id, self.transaction_network_id, self.bank_id, self.amount, self.date, self.transaction_type),
            )
            self.id = cur.fetchone()[0]
        else:
            # Actualizar una transacción existente
            cur.execute(
                "UPDATE transactions SET client_id = %s, account_id = %s, transactions_network_id = %s, bank_id = %s, amount = %s, date = %s, type = %s WHERE id = %s",
                (self.client_id, self.account_id, self.transaction_network_id, self.bank_id, self.amount, self.date, self.transaction_type, self.id),
            )

        # Actualizar el saldo de la cuenta según el tipo de transacción
        if self.transaction_type == "deposit":
            cur.execute(
                "UPDATE accounts SET balance = balance + %s WHERE id = %s",
                (self.amount, self.account_id)
            )
        elif self.transaction_type == "withdraw":
            cur.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (self.amount, self.account_id)
            )
        elif self.transaction_type == "transfer":
            cur.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (self.amount, self.account_id)
            )

        conn.commit()
        disconnect(conn)