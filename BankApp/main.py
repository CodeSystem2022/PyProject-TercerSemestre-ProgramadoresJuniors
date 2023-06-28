from bank.registro import registro
from bank.transaction import transaction
import os

def show_menu(codigo):
    os.system("cls") # limpia la consola
    print(f'\t\t ** su codigo: {codigo} **\n') if codigo is not None else None
    print("********** MENU **********")
    print("1. Realizar depósito")
    print("2. Realizar retiro")
    print("3. Realizar transferencia")
    print("4. ¿No tienes una cuenta? Regístrate")
    print("5. Salir")
    print("***************************")



# Variables auxiliares
codigo = None


# Loop principal
while True:
    
    show_menu(codigo)
    option = input("Selecciona una opción: ")

    if option == "1":
        # Lógica para realizar depósito
        codigo = transaction(codigo, 'deposit')

    elif option == "2":
        # Lógica para realizar retiro
        codigo = transaction(codigo, 'withdraw')
    elif option == "3":
        # Lógica para realizar transferencia
        pass
    elif option == "4":
        # Lógica para realizar registro
        codigo =registro()
        
    elif option == "5":
        # Lógica para despedirse o.O
        print("¡Hasta luego! Banco ProJunior")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
