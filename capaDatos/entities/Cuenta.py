from conection.logger_base import log

class Cuenta:
    def __init__(self, nombre='', apellido='', email='', password='', saldo=0.0):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password = password
        self._saldo = saldo

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre

        @property
        def apellido(self):
            return self._apellido

        @apellido.setter
        def apellido(self, apellido):
            self._apellido = apellido

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, email):
            self._email = email

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, password):
            self._password = password

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            self._saldo = saldo

        @classmethod
        def depositarDinero(self, ingreso):
            ingreso = float(input('Cantidad de dinero a ingresar: '))
            if ingreso > 0:
                self._saldo += ingreso
                log.info('Depósito realizado con éxito')
            else:
                log.error('Ingrese monto válido')

        @classmethod
        def retirarDinero(self, retiro):
            retiro = float(input('Cantidad de dinero a retirar: '))
            if retiro > 0:
                if retiro > self._saldo:
                    log.error('El monto excede sus fondos')
                else:
                    self._saldo -= retiro
                    log.info('Retiro realizado con éxito')
            else:
                log.error('Por favor ingrese un monto válido')

        @classmethod
        def consultarSaldo(self):
            log.info(f'El saldo actual es: {self._saldo}')

