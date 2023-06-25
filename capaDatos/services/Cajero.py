from entities.Cuenta import Cuenta
from conection.logger_base import log
class Cajero:
    def __init__(self):
        self._cuentas = []
        self._valorMenu1 = ''
        self._valorMenu2 = ''
        self._salir = False
        self._volver = False

    @classmethod
    def crearCuenta(self):
        log.debug('Creando nueva cuenta')
        print('Nombre: ')
        nombre = input()
        print('Apellido: ')
        apellido = input()
        print('Email: ')
        email = input()
        print("Password:")
        password = input()
        saldo = 0.0
        cuenta = Cuenta(nombre, apellido, email, password, saldo)
        self._cuentas.append(cuenta)
        print('Cuenta creada exitosamente')

    @classmethod
    def menuDelCajero(self):
        log.debug('Ininciando menú del Cajero')
        self._salir = False
        while not self._salir:
            print("---JUNIORS-BANK---")
            print("1.Nueva cuenta")
            print("2.Ingresar")
            print("3.Salir")
            print("4.Mostrar cuentas")
            print("---JUNIORS-BANK---")
            print("Digite una opción: ")
            self._valorMenu1 = input()
            if self._valorMenu1 == "1":
                self.crearCuenta()
            elif self._valorMenu1 == "2":
                self.ingresar()
            elif self._valorMenu1 == "3":
                self._salir = True
            elif self._valorMenu1 == "4":
                print("-----CUENTAS-----")
                for cuenta in self.cuentas:
                    print("Nombre:", cuenta.nombre, cuenta.apellido,
                          "Email:", cuenta.email, "Saldo:", cuenta.saldo)
            else:
                print("Digite una opción válida")

        @classmethod
        def ingresar(self):
            print("Nombre:")
            name = input()
            print("Password:")
            passw = input()
            cuenta = None
            for a in self._cuentas:
                if name == a.nombre and passw == a.password:
                    cuenta = a
                    self.menuCuenta(cuenta)
                    break
            else:
                print("El usuario o contraseña no coinciden")

        @classmethod
        def eliminarCuenta(self):
            log.debug('Eliminando cuenta')
            print("Ingrese el nombre de la cuenta a eliminar:")
            name = input()
            print("Ingrese el password de la cuenta a eliminar:")
            passw = input()
            cuenta = None
            for a in self._cuentas:
                if name == a.nombre and passw == a.password:
                    cuenta = a
                    print("Su cuenta ha sido eliminada exitosamente")
                    self._cuentas.remove(cuenta)
                    self.menuDelCajero()
                    break
            else:
                print("El usuario o contraseña no coinciden")

        @classmethod
        def menuCuenta(self, cuenta1):
            log.debug(f'Iniciando menú de la cuenta: {cuenta1._nombre}')
            self._volver = False
            while not self._volver:
                print("-----BIENVENIDO-----")
                print(cuenta1._nombre)
                print("---JUNIORS-BANK---")
                print("1.Depositar")
                print("2.Retirar")
                print("3.Consultar saldo")
                print("4.Eliminar cuenta")
                print("5.Salir de la cuenta")
                print("---JUNIORS-BANK---")
                print("Digite una opción:")
                self._valorMenu2 = input()
                if self._valorMenu2 == "1":
                    cuenta1.depositarDinero(0)
                elif self._valorMenu2 == "2":
                    cuenta1.retirarDinero(0)
                elif self._valorMenu2 == "3":
                    cuenta1.consultarSaldo()
                elif self._valorMenu2 == "4":
                    self.eliminarCuenta()
                elif self._valorMenu2 == "5":
                    self._volver = True
                    self.menuDelCajero()
                else:
                    print("Digite una opción válida")
