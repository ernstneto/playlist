from src.view.first_view import introduction_page

def start() -> None:
  while True:
    #introduction_page()
    """
    command = input("Opção desejado: ")
    if command == '1': print("Inserindo música")
    elif command == '2': print("Criando Playlist")
    elif command == '5': exit()
    else: print("\nComando inválido\n\n")
    """
    command = introduction_page()
    if command == '1': print("\nInserindo música\n")
    elif command == '2': print("\nCriando Playlist\n")
    elif command == '5': exit()
    else: print("\nComando inválido\n\n")