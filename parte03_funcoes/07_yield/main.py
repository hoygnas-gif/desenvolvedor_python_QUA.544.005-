# Selecione a biblioteca
from modulo import eq_2o_grau, limpar

def main():
    limpar()

    a = float(input("Informe o valor de a:").replace(",","."))
    b = float(input("Informe o valor de b:").replace(",","."))
    c = float(input("Informe o valor de c:").replace(",","."))
    
    limpar()
    if a != 0:
        result = eq_2o_grau(a,b,c)
        print("Resultado de equação (a,b,c:)")
        for x in result:
            print(f" x= {x}")

    else:    
        print ("Valores informados não são de equação do 2° grau.")
if __name__ == "__main__":
    main()