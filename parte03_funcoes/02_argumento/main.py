#biblioteca
import os

# declaração de funções

def boas_vindas(nome):
    print (f"{nome}, seja bem_vindo!")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# algoritimo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)

