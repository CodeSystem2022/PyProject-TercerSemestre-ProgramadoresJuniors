from .postgres import connect, disconnect
from .logging.logger_base import log
import random


class Account:
    def __init__(self, balance, client_id, bank_id, account_number=None):
        self.id = None  # ID generado automáticamente por la base de datos
        self.client_id = client_id
        self.balance = balance
        self.bank_id = bank_id
        self.account_number = account_number or random.randint(10000, 99999)
        # Guardar el objeto en la base de datos
        #self.save()

    # Método para guardar la cuenta creada en la base de datos  y crear ID
    def save(self):
        try:
            conn = connect()
            cur = conn.cursor()

            if self.id is None:
                #print(self.client_id)
                # Insertar una nueva cuenta y obtener el ID generado
                cur.execute("INSERT INTO accounts (balance, client_id, bank_id, account_number) VALUES (%s,%s,%s,%s) RETURNING id", (self.balance, self.client_id, self.bank_id, self.account_number))
                self.id = cur.fetchone()[0]
            else:
                # Si el ID existe entonces solo le cambia el balance
                cur.execute("UPDATE accounts SET (balance, client_id, bank_id, account_number) = (%s,%s,%s,%s) WHERE id = %s", (self.balance, self.client_id, self.bank_id, self.account_number, self.id))

            conn.commit()
        except Exception as e:
                log.error(e)
        finally:
            disconnect(conn)

    # Método para traer todas las cuentas
    @staticmethod
    def get_all():
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM accounts")
            rows = cur.fetchall()
        except Exception as e:
             log.error(e)
        finally:
            disconnect(conn)
            

            accounts = []
            for row in rows:
                account_id, balance = row
                account = Account(balance)
                account.id = account_id
                accounts.append(account)
            return accounts
    
    @staticmethod
    def get_by_id(account_id):
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))
            row = cur.fetchone()
        except Exception as e:
                log.error(e)
        finally:
            disconnect(conn)

        if row:
            account_id, client_id, account_number, balance, bank_id = row
            account = Account(float(balance), client_id, bank_id, account_number)
            account.id = account_id
            return account
        return None
    
    @staticmethod
    def get_by_account_number(account_number):
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM accounts WHERE account_number = %s", (str(account_number),))
            row = cur.fetchone()
        except Exception as e:
            log.error(e)
        finally:
            disconnect(conn)

        if row:
            account_id, client_id, account_number, balance, bank_id  = row
            account = Account(float(balance), client_id, bank_id, account_number)
            account.id = account_id
            return account
        return None
        