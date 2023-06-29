from models.banks import Bank
from models.clients import Client
from models.accounts import Account
from models.logging.logger_base import log
import time
import os


# Loader visual para que se vea mas bonito owo
def loader(duration):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            break
        for char in "/-\|":
            print(f"Loading... {char}", end="\r")
            time.sleep(0.1)


def registro():
    os.system("cls")  # limpia la consola

    print("\t\t** Elija un Banco **\n")
    loader(3)

    ##################################  Bancos  ##################################

    # Trae los bancos y los muestra
    banks_list = Bank.get_all()
    for bank in banks_list[30:44]:
        print(f"{bank._id}. {bank._name}")
    print("\n")

    # Nos aseguramos que el id ingresado sea correcto
    while True:
        bank_id = input("")
        if bank_id.isdigit() and 1 <= int(bank_id) <= 10:
            break
        else:
            os.system("cls")  # limpia la consola
            print("\t\t** Elija un Banco **\n")
            print("ERROR: Ingrese un número de Banco válido\n")
            for bank in banks_list[30:44]:
                print(f"{bank._id}. {bank._name}")
            print("\n")

    ################################## Cliente y Cuenta ##################################
    os.system("cls")  # limpia la consola
    print("\t\t ** Ingrese su informacion personal **\n")
    name = input("name: ")
    address = input("address: ")
    phone = input("phone: ")

    ################################## Carga en la Base de Datos ##################################
    os.system("cls")  # limpia la consola
    loader(3)
    os.system("cls")
    try:
        # Creamos y guardamos en la base de datos
        cliente = Client(name, address, phone, bank_id)
        cliente.save()

        cuenta = Account(0.0, cliente._id, bank_id)
        cuenta.save()

        # Mensaje de exito
        print("\t\t ¡Su cuenta se ha creado con éxito!\n\n")
        print(f"Su número de cuenta: {cuenta._account_number}")
        input("")
        os.system("cls")  # limpia la consola
        return cuenta._account_number
    except:
        log.info("Error al crear cuenta. Contacte a su banco")

        return None
