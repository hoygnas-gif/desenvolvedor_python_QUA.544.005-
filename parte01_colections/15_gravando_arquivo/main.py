#bibliotecas
#NOTE - jason = (JavaScript Object notation) ou (Objeto de notação JavaScrip
#NOTE - o tipo de arquivo JASON conversa muito bem com pyton, mesmo sendo um arquivo JavaScrip

import os
import json

usuarios = []
os.system("cls"if os.name == "nt" else "clean")

# abrir ler e sair

while True:
    print("Opção 01 - cadastrar novo usuario")
    print("Opção 01 - criar ou gravar arquivo JASON")
    print("Opção 03 - Ler o arquivo JSON")
    print("Opção 04 - Sair do programa")
    menu = input("Qual a opção desejada: ")
    match menu:
        case "1":
            #Novo Dicionario

            usuario = { }

            # insersão dos dados no dicionario

            usuario['nome'] = inpurt("Insira o seu nome: ").strip().title()
            usuario['idade'] = int(input("Insira sua idade: "),strip())
            usuario['email'] = input("Insira o seu email: ").strip().lower()
            usuario['cpf'] = input("Insira seu CPF: ").strip()
            usuario['Telefone'] = input("Insirao seu telefone: ").strip()

            #Insersão de dados no dicionario

            usuario.append(usuario)

            os.system("cls" if os.name == elde "clean")

            # mensagem de confirmação
            print(f"{usuario.get('nome')} cadastrado com sucesso")
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{"-"*40"}")
                      
            tobecon = input("Deseja gravar os dados? (s/n): ").lowe()
            #NOTE - o json é de arquivos  .jason, ja o f. é de arquivos .txt
            tobecon == "s":
            os.system