from .postgres import connect, disconnect
import random


class Account:
    def __init__(self, balance, client_id, bank_id):
        self.id = None  # ID generado automáticamente por la base de datos
        self.client_id = client_id
        self.balance = balance
        self.bank_id = bank_id
        self.account_number = random.randrange(10000, 100000)
        # Guardar el objeto en la base de datos
        #self.save()

    # Método para guardar la cuenta creada en la base de datos  y crear ID
    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar una nueva cuenta y obtener el ID generado
            cur.execute("INSERT INTO accounts (balance) VALUES (%s) RETURNING id", (self.balance,))
            self.id = cur.fetchone()[0]
        else:
            # Si el ID existe entonces solo le cambia el balance
            cur.execute("UPDATE accounts SET balance = %s WHERE id = %s", (self.balance, self.id))

        conn.commit()
        disconnect(conn)

    # Método para traer todas las cuentas
    @staticmethod
    def get_all():
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts")
        rows = cur.fetchall()
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
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))
        row = cur.fetchone()

        disconnect(conn)

        if row:
            account_id, client_id, account_number, balance, bank_id = row
            account = Account(client_id, account_number, balance, bank_id)
            account.id = account_id
            return account
        return None
    
    