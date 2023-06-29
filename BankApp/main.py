from bank.registro import registro
from bank.transaction import transaction
from bank.transferce import transfer_account_to_account
from bank.main_menu import show_menu
from bank.baybay import despedida
from models.logging.logger_base import log

# Variables auxiliares
codigo = None

# Loop principal
while True:
    show_menu(codigo)
    option = input("Selecciona una opción: ")

    if option == "1":
        # Lógica para realizar depósito
        codigo = transaction(codigo, "deposit")
    elif option == "2":
        # Lógica para realizar retiro
        codigo = transaction(codigo, "withdraw")
    elif option == "3":
        # Lógica para realizar transferencia
        codigo = transfer_account_to_account(codigo)
    elif option == "4":
        # Lógica para realizar registro
        codigo = registro()
    elif option == "5":
        # Lógica para despedirse o.O
        despedida()
        break
    else:
        log.info("Opción inválida. Por favor, selecciona una opción válida.")
