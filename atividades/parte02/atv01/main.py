# TODO: parte 02 atividade 01
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um .json
- Abre arquivo .json e lista todos os usuários cadastrados nele
"""
#TODO- Cadastrar novo usuario:

import os
import json

usuarios = []

while True:
    print("\n--- CADASTRO DE USUÁRIOS ---")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("5 - Salvar usuários")
    print("6 - Abrir arquivo JSON")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").strip()
        cpf = input("CPF: ").strip()

        usuario = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(usuarios, start=1):
                print(f"\n--- Usuário {i} ---")
                print(f"Nome: {usuario['nome']}")
                print(f"E-mail: {usuario['email']}")
                print(f"Telefone: {usuario['telefone']}")
                print(f"CPF: {usuario['cpf']}")

    elif opcao == "3":
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i} - {usuario['nome']}")

        if usuarios:
            numero = int(input("Número do usuário para alterar: ")) - 1

            if 0 <= numero < len(usuarios):
                usuario = usuarios[numero]

                nome = input("Novo nome (Enter mantém): ").strip()
                email = input("Novo e-mail (Enter mantém): ").strip()
                telefone = input("Novo telefone (Enter mantém): ").strip()
                cpf = input("Novo CPF (Enter mantém): ").strip()

                if nome:
                    usuario["nome"] = nome
                if email:
                    usuario["email"] = email
                if telefone:
                    usuario["telefone"] = telefone
                if cpf:
                    usuario["cpf"] = cpf

                print("Usuário alterado com sucesso!")
            else:
                print("Número inválido.")
        else:
            print("Nenhum usuário cadastrado.")

    elif opcao == "4":
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i} - {usuario['nome']}")

        if usuarios:
            numero = int(input("Número do usuário para excluir: ")) - 1

            if 0 <= numero < len(usuarios):
                usuarios.pop(numero)
                print("Usuário excluído com sucesso!")
            else:
                print("Número inválido.")
        else:
            print("Nenhum usuário cadastrado.")

    elif opcao == "5":
        with open("usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

        print("Usuários salvos com sucesso!")

    elif opcao == "6":
        try:
            with open("usuarios.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)

            print("Usuários carregados do arquivo!")

            for i, usuario in enumerate(usuarios, start=1):
                print(f"\n--- Usuário {i} ---")
                print(f"Nome: {usuario['nome']}")
                print(f"E-mail: {usuario['email']}")
                print(f"Telefone: {usuario['telefone']}")
                print(f"CPF: {usuario['cpf']}")

        except FileNotFoundError:
            print("Arquivo não encontrado. Salve os usuários primeiro.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
