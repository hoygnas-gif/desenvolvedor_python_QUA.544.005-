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

import os
import json

usuarios = []

def cadastrar_usuarios():
    nome =input("Nome: "). strip()
    email =input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()
    cpf = input("CPF: ").strip()
    usuario = {
                  "nome": nome,
                  "email": email,
                  "telefone": telefone,
                  "cpf": cpf,
            }
    usuarios.append(usuario)
    print("Usuario cadastros com sucesso!")

cadastrar_usuarios()
print (usuarios)

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado")
        return
    
    for i,usuario in enumerate(usuarios, start=1):
        print(f"\n--- Usuário {i} --- ")
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Telefone: {usuario['telefone']}")
        print(f"CPF: {usuario['cpf']}")
