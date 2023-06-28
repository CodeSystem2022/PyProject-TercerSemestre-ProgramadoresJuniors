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
