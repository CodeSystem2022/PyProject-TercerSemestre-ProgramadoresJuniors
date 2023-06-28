from .postgres import connect, disconnect

class Bank:
    def __init__(self, name, network_type_id):
        self.id = None  # ID generado automáticamente por la base de datos
        self.name = name
        self.network_type_id = network_type_id

        # Guardar la instancia automáticamente
        #self.save()

    def save(self):
        conn = connect()
        cur = conn.cursor()

        if self.id is None:
            # Insertar un nuevo banco y obtener el ID generado
            cur.execute("INSERT INTO banks (name, network_type_id) VALUES (%s, %s) RETURNING id", (self.name, self.network_type_id))
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
        #print(rows)
        for row in rows:
            bank_id, name, network = row
            bank = Bank(name, network)
            bank.id = bank_id
            banks.append(bank)

        return banks
    
    @staticmethod
    def get_by_id(bank_id):
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM banks WHERE id = %s", (bank_id,))
        row = cur.fetchone()

        disconnect(conn)

        if row:
            bank_id, name, network_type_id = row
            bank = Bank(name, network_type_id)
            bank.id = bank_id
            return bank

        return None