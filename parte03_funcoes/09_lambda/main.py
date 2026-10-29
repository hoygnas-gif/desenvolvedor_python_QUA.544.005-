import os

# lambdas
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
area_triangulo = lambda b,h: (b*h)/2

#função principal
def main():
    limpar()
    b = float(input("Iforme a base: ").replace(",","."))
    h = float(input("Iforme a altura: ").replace(",","."))
    limpar()
    print(f"Àrea do triangulo:{area_triangulo(b,h)}.")


if __name__ == "__main__":
    main()
