from models.accounts import Account
from bank.registro import loader
from bank.transaction import transaction
from models.Transaction import Transaction
from models.banks import Bank
from models.logging.logger_base import log
import os

def transfer_account_to_account(codigo):
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

    # Una vez pasada la autenticación pasamos a realizar la transferencia

    # Pedimos datos de monto y receptor
    while True:
        os.system("cls") # limpia la consola
        print('\t\t** Ingrese monto a transferir **\n')
        ammount = input('')
        if int(ammount) > 0:
            break

    os.system("cls") # limpia la consola
    print('\t\t** Ingrese ID de la entidad que recibe **\n')
    receptor_id = input('')
    loader(2)


    # Lógica para hacer transferencia
    try:
        receptor = Account.get_by_id(str(receptor_id))
        

        ##################################### Retirar plata al que envía #####################################
        # ID del que envía
        client_id = account.client_id
        account_id = account.id

        # Banco
        bank_id = account.bank_id
        bank_from_account = Bank.get_by_id(bank_id)
        transaction_network_id = bank_from_account.network_type_id

        # Transacción
        transaction_type = 'transfer'

        transaction_transfer = Transaction(client_id,
                                account_id,
                                transaction_network_id,
                                bank_id,
                                ammount,
                                transaction_type
                                )
        transaction_transfer.save()

        ##################################### Ingresar plata a la cuenta del receptor #####################################
        # ID del que envía
        client_id = receptor.client_id
        account_id = receptor.id

        # Banco
        bank_id = receptor.bank_id
        bank_from_receptor = Bank.get_by_id(bank_id)
        transaction_network_id = bank_from_receptor.network_type_id

        # Transacción
        transaction_type = 'deposit'

        transaction = Transaction(client_id,
                                receptor_id,
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
                Monto: {transaction_transfer.amount}\n \
               -------------------------------------\n \
               Tipo: {transaction_transfer.transaction_type}\n \
               Fecha: {transaction_transfer.date}\n \
               id: {transaction_transfer.id}\n \
              ')
        input('')

    except:
        #print('No se pudo realizar la trasnferencia')
        log.info('No se pudo realizar la trasnferencia')

    finally:
        return account.account_number 