# bibliotecas
import os


# lista vazia
tarefas = []


# lista terminal
os.system("cls" if os.name == "nt" else "clear")
# loop
while True:
    # menu
    print("1 - inserir nova tarefa na lista")
    print("2 - finalizar e exibir lisga")
    opcao = input("opcao desejada: ").strip() #informa a opção desejada

# verificar opção informada
    match opcao:
        case "1":
            nova_tarefa = input("informe a nova terefa: ")  # usuario informa item da lista
            tarefas.append(nova_tarefa) #inserem item na lista
            continue #retorna para inicio do loop
        case "2":
            os.system("cil" if os.name == "nt" else "clear")
        case _:
            print("opção inválida.")

    # exibe a lista
    for n, tarefa in enumerate(tarefas, start=1):
        print(f"{n}ª tarefa: {tarefa}")
        break # encerra o loop
