# dicionario
usuario = {
    'nome':"Hoygna Souza",
    'idade': 33,
    'altura': 1.66,
    'email' : "hoygnas@gmail.com",
    'cpf' : "222.222.555.16",
    'telefone': "(61) 98765-4321"
}

# exibe valor especifico
print(f"Nome:{usuario['nome']}")
print(f"E-mail: {usuario.get('email')}")

#percorre o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")