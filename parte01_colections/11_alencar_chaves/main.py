# biblioteca
import os

# dicionario
usuario = {
    'nome': "Thomaz Anderson",
    'idade': 40,
    'email': "mranderson@gmail.com",
    'telefone': "(61) 9666-6666"
    }

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # exibe o dicionario
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

      # informar o nomem da chave
    chave_escolhida = input("informe o nomes da chave que deseja alterar ou enter para Encerrar:").strip().lower()
        # verifica se a chave é válida
    if chave_escolhida:
        # informa o novo valor
        usuario[chave_escolhida] = input("Informe o novo valor: ").strip()
        continue
    else:
          
        break