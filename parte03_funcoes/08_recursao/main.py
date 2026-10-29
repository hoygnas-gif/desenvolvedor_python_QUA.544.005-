# biblioteca 
import os


# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#funções recursiva
def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

#função principal
def main():
    limpar()
    try:
        n = int(input("informe um número inteiro: "))
        limpar()
        print(F"fatorial de {n}! é {fatorial(n)}.")
    except Exception as e:
        print(f"Não foi possível calcular o fatrial;{e};")
if __name__ == "__main__":
    main()