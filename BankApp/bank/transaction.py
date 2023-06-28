from models.accounts import Account
from models.banks import Bank
from models.Transaction import Transaction
from bank.registro import loader
import os

def transaction(codigo, transaction_type):
    os.system("cls") # limpia la consola
    if codigo is not None:
        print(f'\t\t** Hemos detectado su código de usuario {codigo}**\n')
        account = Account.get_by_account_number(codigo)
    else:
        # Inicio de sesión con codigo de usuario
        while True:
            codigo = input('ingrese su codigo de usuario: ')
            os.system("cls") # limpia la consola
            account = Account.get_by_account_number(codigo)
            if account is not None:
                break
            else:
                print('\t\t** Ingrese un código válido ** \n')


    # Una vez pasada la autenticación pasamos a realizar el depósito
    while True:
        os.system("cls") # limpia la consola
        print('\t\t** Ingrese monto **\n')
        ammount = input('')
        loader(2)
        if ammount >= 0:
            break
   
   
    # Obteniendo datos necesarios para transacción
    # ID
    client_id = account.client_id
    account_id = account.id

    # Banco
    bank_id = account.bank_id
    bank_from_account = Bank.get_by_id(bank_id)
    transaction_network_id = bank_from_account.network_type_id

    # Transacción
    transaction_type = transaction_type

    # Finalmente realizamos la transacción
    try:
        transaction = Transaction(client_id,
                                account_id,
                                transaction_network_id,
                                bank_id,
                                ammount,
                                transaction_type
                                )
        transaction.save()

        # Detalles de la transacción
        os.system("cls") # limpia la consola
        print(f'\t\t** Transacción Realizada **\n \
                Banco: {bank_from_account.name}\n \
                Cuenta: {account.account_number}\n \
                Monto: {transaction.amount}\n \
               -------------------------------------\n \
               Tipo: {transaction.transaction_type}\n \
               Fecha: {transaction.date}\n \
               id: {transaction.id}\n \
              ')
        input('')
    except:
        print('Error al realizar la transacción')

    finally:
        # Retornamos el numero de cuenta asi queda guardado el inicio de sesión
        return account.account_number 