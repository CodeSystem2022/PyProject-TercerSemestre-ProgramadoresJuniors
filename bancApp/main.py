from capaDatos.entities import CuentaDAO, Cuenta


def main():
    dao = CuentaDAO()

    # Crear una cuenta
    cuenta = Cuenta(nombre='John', apellido='Doe', email='john@example.com', password='123456', saldo=0)
    dao.crear_cuenta(cuenta)

    # Eliminar una cuenta
    cuenta = dao.obtener_cuenta_por_nombre('John')
    dao.eliminar_cuenta(cuenta)

if __name__ == '__main__':
    main()
