# biblioteca
import os


# lista
nomes = ["Alex", "Charlote", "Scarlatet", "jhon", "Michael", "Connor"]

os.system("cls" if os.name == "nt" else "clear")
# loop
while True:
    for n, nome in enumerate(nomes):
        print(f"indice {n}: {nome}")
    #menu
    print("1 - Alterar item da lista")
    print("2 - Finalizar")
    opcao = input("opcao desejada: ").strip() #informa a opção desejada

    # verifica a opção escolhida
    match opcao:
        case "1":
            # informa o indice a sere alterado
            indice = int(input("informe o indice a ser alterado: "))
            #informa novo valor 
            nomes[indice] = input("informe novo nome: ").strip().title()
            os.system("cls" if os.name == "nt" else "clear")
        # exibe a nova lista
        case _:
            print('opção invalid')
            continue