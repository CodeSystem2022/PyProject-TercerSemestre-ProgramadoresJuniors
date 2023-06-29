from models.accounts import Account
from bank.registro import loader
from bank.transaction import transaction
from models.Transaction import Transaction
from models.banks import Bank
from models.logging.logger_base import log
import os


def transfer_account_to_account(codigo):
    os.system("cls")  # limpia la consola
    if codigo is not None:
        print(f"\t\t** Hemos detectado su código de usuario {codigo}**\n")
        account = Account.get_by_account_number(codigo)
    else:
        # Inicio de sesión con codigo de usuario
        while True:
            codigo = input("ingrese su codigo de usuario: ")
            os.system("cls")  # limpia la consola
            account = Account.get_by_account_number(codigo)
            if account is not None:
                break
            else:
                print("\t\t** Ingrese un código válido ** \n")

    # Una vez pasada la autenticación pasamos a realizar la transferencia

    # Pedimos datos de monto y receptor
    while True:
        os.system("cls")  # limpia la consola
        print("\t\t** Ingrese monto a transferir **\n")
        ammount = input("")
        if int(ammount) > 0:
            break

    os.system("cls")  # limpia la consola
    print("\t\t** Ingrese ID de la entidad que recibe **\n")
    receptor_id = input("")
    loader(2)

    # Lógica para hacer transferencia
    try:
        receptor = Account.get_by_id(str(receptor_id))

        ##################################### Retirar plata al que envía #####################################
        # ID del que envía
        client_id = account._client_id
        account_id = account._id

        # Banco
        bank_id = account._bank_id
        bank_from_account = Bank.get_by_id(bank_id)
        transaction_network_id = bank_from_account._network_type_id

        # Transacción
        transaction_type = "transfer"

        transaction_transfer = Transaction(
            client_id,
            account_id,
            transaction_network_id,
            bank_id,
            ammount,
            transaction_type,
        )
        transaction_transfer.save()

        ##################################### Ingresar plata a la cuenta del receptor #####################################
        # ID del que envía
        client_id = receptor._client_id
        account_id = receptor._id

        # Banco
        bank_id = receptor._bank_id
        bank_from_receptor = Bank.get_by_id(bank_id)
        transaction_network_id = bank_from_receptor._network_type_id

        # Transacción
        transaction_type = "deposit"

        transaction = Transaction(
            client_id,
            receptor_id,
            transaction_network_id,
            bank_id,
            ammount,
            transaction_type,
        )
        transaction.save()

        # Detalles de la transacción
        os.system("cls")  # limpia la consola
        print(
            f"\t\t** Transacción Realizada **\n"
            f"    Banco: {bank_from_account._name}\n"
            f"    Cuenta: {account._account_number}\n"
            f"    Monto: {transaction_transfer._amount}\n"
            f"    Saldo Actual: {account._balance}\n"
            f"   -------------------------------------\n"
            f"   Tipo: {transaction_transfer.transaction_type}\n"
            f"   Fecha: {transaction_transfer._date}\n"
            f"   id: {transaction_transfer._id}\n"
        )
        input("")

    except:
        # print('No se pudo realizar la trasnferencia')
        log.info("No se pudo realizar la trasnferencia")

    finally:
        return account._account_number