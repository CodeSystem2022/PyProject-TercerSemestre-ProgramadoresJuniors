from models.banks import Bank
from models.clients import Client
from models.accounts import Account

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

def show_menu():
    print("********** MENU **********")
    print("1. Realizar depósito")
    print("2. Realizar retiro")
    print("3. Realizar transferencia")
    print("4. ¿No tienes una cuenta? Regístrate")
    print("5. Salir")
    print("***************************")

def registro():
    os.system("cls") # limpia la consola

    print('\t\t** Elija un Banco **\n')
    loader(3)
    
##################################  Bancos  ##################################

    # Trae los bancos y los muestra
    banks_list = Bank.get_all()
    for bank in banks_list[:10]:
        print(f'{bank.id}. {bank.name}')
    print('\n')

    # Nos aseguramos que el id ingresado sea correcto
    while True:
        bank_id = input('')
        if bank_id.isdigit() and 1 <= int(bank_id) <= 10:
            break
        else:
            os.system("cls") # limpia la consola
            print('\t\t** Elija un Banco **\n')
            print('ERROR: Ingrese un número de Banco válido\n')
            for bank in banks_list[:10]:
                print(f'{bank.id}. {bank.name}')
            print('\n')
    

################################## Cliente y Cuenta ##################################
    os.system("cls") # limpia la consola
    print('\t\t ** Ingrese su informacion personal **\n')
    name = input('name: ')
    address = input('address: ')
    phone = input('phone: ')


################################## Carga en la Base de Datos ##################################
    os.system("cls") # limpia la consola
    loader(3)
    os.system("cls")
    try:
        #Creamos y guardamos en la base de datos
        cliente = Client(name, address, phone, bank_id)
        cliente.save()

        cuenta = Account(0.0, cliente.id, bank_id)
        cuenta.save()

        # Mensaje de exito
        print('\t\t ¡Su cuenta se ha creado con éxito!\n\n')
        print(f'Su número de cuenta: {cuenta.account_number}')
    except:
        print('Error al crear cuenta. Contacte a su banco')
        


            


# Loop principal
while True:
    show_menu()
    option = input("Selecciona una opción: ")

    if option == "1":
        # Lógica para realizar depósito
        pass
    elif option == "2":
        # Lógica para realizar retiro
        pass
    elif option == "3":
        # Lógica para realizar transferencia
        pass
    elif option == "4":
        # Lógica para realizar registro
        registro()
        
    elif option == "5":
        print("¡Hasta luego! Banco ProJunior")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
