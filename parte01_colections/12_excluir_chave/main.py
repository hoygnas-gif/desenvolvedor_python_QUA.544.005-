# dicionario
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'email': "(61)98765-4321",
    'telefone': "(61) 9 98765-4321",
    'endereço': "Campo da esperança"
}

# exibir a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

print("")
#informa a chave a ser deletada
chave_escolhida = input("informe a chave a excluir: ").strip().lower()

# deleta a chave
del usuario[chave_escolhida]
#re-exibe o novo dicionario
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

