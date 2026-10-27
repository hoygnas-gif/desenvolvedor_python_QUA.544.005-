# dicionario
usuario = {
'nome': "Fulano de Tal",
'idade': 33,
'email': "hoygnas@gmail,com", 
}

# usuario informar o nome sda nova chave
nova_chave = input("informe o nome da nova chave: ").strip().lower()
# usuario informa o nome da nova chave
usuario[nova_chave] = input("informe o valor da nova chave: ").strip()

# exibe o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}:{valor}.")
