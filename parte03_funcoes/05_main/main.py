# selection - biblioteca
import math
import os


# funções - caucular raiz
def raiz(n):
    return math.sqrt(n)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Algoritimo principal - usado para não importar o codigo entre a transição de programa para o outro
def main():
    limpar()
    n = int(input("Informe um número inteiro: "))
    print(f"Raiz de {n} é {raiz(n)}.")

    

# ALGORITIMO PRINCIPAL PROTEGIDO
if __name__ == "__main__":
    main()