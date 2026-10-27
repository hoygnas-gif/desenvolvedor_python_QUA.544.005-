# Cadastra novo usuário (nome, email, telefone, cpf)
 #Lista todos os usuários cadastrados
 #Altera os dados de um usuário
 #Exclui um usuário
 #Grava os dados de todos os usuários em um .json
 #Abre arquivo .json e lista todos os usuários cadastrados nele

# Bibliotecas
import os
import time
import json

# Lista de usuarios
usuarios = []

arquivo_json = os.path.join(os.path.dirname(__file__), "usuarios.json")

# Menu principal
while True:
    print("\n" + "-" * 40)
    print("SISTEMA DE CADASTRO DE USUARIOS")
    print("-" * 40)
    print("Opção 1 - Cadastrar novo usuario")
    print("Opção 2 - Listar todos os usuarios")
    print("Opção 3 - Alterar dados de um usuario")
    print("Opção 4 - Excluir um usuario")
    print("Opção 5 - Gravar usuarios em arquivo JSON")
    print("Opção 6 - Ler arquivo JSON")
    print("Opção 7 - Sair do programa")
    print("-" * 40)

    menu = input("Qual a opção desejada: ").strip()

    match menu:

        case "1":
            # Cadastrar novo usuario

            usuario = {}

            usuario["nome"] = input("Insira seu nome: ").strip().title()
            usuario["email"] = input("Insira seu email: ").strip().lower()
            usuario["telefone"] = input("Insira seu telefone: ").strip()
            usuario["cpf"] = input("Insira seu CPF: ").strip()

            usuarios.append(usuario)

            print("Usuario cadastrado com sucesso!")

        case "2":
            # Listar todos os usuarios

            if len(usuarios) == 0:
                print("Nenhum usuario cadastrado.")

            else:
                for indice, usuario in enumerate(usuarios, start=1):
                    print(f"\nUsuario {indice}")

                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                        time.sleep(.25)

                    print("-" * 40)

        case "3":
            # Alterar dados de um usuario pela listagem

            if len(usuarios) == 0:
                print("Nenhum usuario cadastrado.")

            else:
                print("\nLISTA DE USUARIOS")
                print("-" * 40)

                for indice, usuario in enumerate(usuarios, start=1):
                    print(f"{indice} - {usuario['nome']}")

                print("-" * 40)

                escolha = int(input("Digite o numero do usuario que deseja alterar: "))

                if escolha >= 1 and escolha <= len(usuarios):
                    usuario = usuarios[escolha - 1]

                    print("Deixe vazio o campo que não deseja alterar.")

                    nome = input("Novo nome: ").strip()
                    email = input("Novo email: ").strip().lower()
                    telefone = input("Novo telefone: ").strip()
                    cpf = input("Novo CPF: ").strip()

                    if nome != "":
                        usuario["nome"] = nome.title()

                    if email != "":
                        usuario["email"] = email

                    if telefone != "":
                        usuario["telefone"] = telefone

                    if cpf != "":
                        usuario["cpf"] = cpf

                    print("Dados alterados com sucesso!")

                else:
                    print("Numero de usuario invalido.")

        case "4":
            # Excluir um usuario
            escolha = int(input("Digite o numero do usuario que deseja excluir: ").strip())
            
            if escolha >= 1 and escolha <= len(usuarios):
                usuario = usuarios[escolha - 1]

                
                print("Usuario excluido com sucesso!")
                    

                if encontrado == False:
                    print("Usuario não encontrado.")
                else:
                    print("Usuario excluido com sucesso.")
        
        case "5":
            # Gravar usuarios em arquivo JSON

            with open(arquivo_json, "w", encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

            print("Dados gravados no arquivo JSON com sucesso!")
            continue

        case "6":
    # Ler arquivo JSON e listar usuarios

            if os.path.exists(arquivo_json):
                with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                    usuarios_arquivo = json.load(arquivo)

                if len(usuarios_arquivo) == 0:
                    print("O arquivo não possui usuarios cadastrados.")
                else:
                    for usuario in usuarios_arquivo:
                        for chave, valor in usuario.items():
                            print(f"{chave.capitalize()}: {valor}")

                        print("-" * 40)

            else:
                print("Arquivo JSON não encontrado.")
                print("Escolha a opção 5 para gravar os dados primeiro.")
            
        case "7":
            print("Programa encerrado.")
            break

        case _:
            print("Opção invalida. Escolha uma opção de 1 a 7.")
