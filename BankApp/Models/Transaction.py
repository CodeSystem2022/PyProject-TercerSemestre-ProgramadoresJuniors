from datetime import datetime
import psycopg2
from .postgres import connect, disconnect
from .logging.logger_base import log


class Transaction:
    def __init__(
        self,
        client_id,
        account_id,
        transaction_network_id,
        bank_id,
        amount,
        transaction_type,
    ):
        self._id = None  # ID generado automáticamente por la base de datos
        self._client_id = client_id
        self._account_id = account_id
        self._transaction_network_id = transaction_network_id
        self._bank_id = bank_id
        self._amount = amount
        self._transaction_type = transaction_type
        self._date = datetime.now()

    def save(self):
        try:
            conn = connect()
            cur = conn.cursor()

            if self._id is None:
                # Insertar una nueva transacción y obtener el ID generado
                cur.execute(
                    "INSERT INTO transactions (client_id, account_id, transactions_network_id, bank_id, amount, date, type) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
                    (
                        self._client_id,
                        self._account_id,
                        self._transaction_network_id,
                        self._bank_id,
                        self._amount,
                        self._date,
                        self._transaction_type,
                    ),
                )
                self._id = cur.fetchone()[0]
            else:
                # Actualizar una transacción existente
                cur.execute(
                    "UPDATE transactions SET client_id = %s, account_id = %s, transactions_network_id = %s, bank_id = %s, amount = %s, date = %s, type = %s WHERE id = %s",
                    (
                        self._client_id,
                        self._account_id,
                        self._transaction_network_id,
                        self._bank_id,
                        self._amount,
                        self._date,
                        self._transaction_type,
                        self._id,
                    ),
                )

            # Actualizar el saldo de la cuenta según el tipo de transacción
            if self._transaction_type == "deposit":
                cur.execute(
                    "UPDATE accounts SET balance = balance + %s WHERE id = %s",
                    (self._amount, self._account_id),
                )
            elif self._transaction_type == "withdraw":
                cur.execute(
                    "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                    (self._amount, self._account_id),
                )
            elif self._transaction_type == "transfer":
                cur.execute(
                    "UPDATE accounts SET balance = balance - %s WHERE id = %s",
                    (self._amount, self._account_id),
                )

            conn.commit()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)