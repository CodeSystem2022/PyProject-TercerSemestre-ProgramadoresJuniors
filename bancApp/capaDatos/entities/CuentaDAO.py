import sys
from conection.conexion import obtenerConexion, cerrarConexion
class CuentaDAO:
    @classmethod
    def crearCuenta(self, cuenta):
        conexion = obtenerConexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO cuenta (nombre, apellido, email, password, saldo) VALUES (%s, %s, %s, %s, %s)",
                (cuenta.nombre, cuenta.apellido, cuenta.email, cuenta.password, cuenta.saldo)
            )
            conexion.commit()
            print("Cuenta creada exitosamente")
        except Exception as e:
            conexion.rollback()
            print("Error al crear la cuenta:", str(e))
        finally:
            cerrar_conexion(conexion)

    @classmethod
    def eliminarCuenta(self, cuenta):
        conexion = obtenerConexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM cuenta WHERE nombre = %s", (cuenta.nombre,))
            conexion.commit()
            print("Cuenta eliminada exitosamente")
        except Exception as e:
            conexion.rollback()
            print("Error al eliminar la cuenta:", str(e))
        finally:
            cerrarConexion(conexion)

    @classmethod
    def obtenerCuentaPorNombre(self, nombre):
        conexion = obtenerConexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cuenta WHERE nombre = %s", (nombre,))
            cuenta_data = cursor.fetchone()
            if cuenta_data:
                cuenta = Cuenta(*cuenta_data)
                return cuenta
            else:
                return None
        except Exception as e:
            print("Error al obtener la cuenta:", str(e))
        finally:
            cerrarConexion(conexion)