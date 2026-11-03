# TODO: parte 03 atividade 02
'''
crie um programa em que o usuário informe um número inteiro e o programa retorne a sequencia fibonacci.
'''
# biblioteca

# função
def fibonacci(numero):
    a = 0
    b = 1

    for i in range(numero):
        print(a, end=" ")

        proximo = a + b
        a = b
        b = proximo


# programa principal
def main():
    numero = int(input("Informe um número inteiro: "))

    if numero > 0:
        print("Sequência de Fibonacci:")
        fibonacci(numero)
    else:
        print("Informe um número inteiro positivo.")


if __name__ == "__main__":
    main()
