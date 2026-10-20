# lista
frutas = [
    "Maça", 
    "Pera",
    "Maracuja",
    "Morango", 
    "Manga",
    "Melancia",
    "Goiaba",
]

while True:
    for n, fruta in enumerate(frutas):
        print(f"indice {n}: {fruta}")

    # menu
    print("1 - fruta")
    print("2 - encerrar programa")
    opcao = input("opção desejada: ").strip()
    # Verifica opção
    match opcao:
        case "1":
            indice = int(input("informe o indice a ser excluido: "))
            del(frutas[indice]) # exclui  indice selecionado
            print('\nFrutas excluida com sucesso!\n')
            continue
        case '2':
            break
        case _:
            print("Opção invalida.")
            continue