# importa o módulo
import modulo


#algoritimo principal
modulo.limpar()
while True:
    print("1 - calcular área do quadrilátero")
    print("2 - calcular área do circulo")
    print("3 - calcular cumprimento do círculo")
    print("4 - sair do programa")
    opcao = input("opção desejada: ").strip()
    modulo,limpar()
    match opcao:
        case "1":
            b = float(input("Informe a base: ").replace(",","."))
            h = float(input("Informe a altura: ").replace(",","."))
            a = modulo.a_quad(b,h)
            print(f"Àrea dp quadrilatero: {a}.")
            continue
        case "2":
            r = float(input("Informe o raio: ").replace(",", "."))
            a = modulo.a_circulo(r)
            print(f"Àrea do circulo:{a}.")
            continue
        case "3":
            r = float(input("Informe o raio: ").replace(",","."))
            a = modulo.comprimento_circulo(r)
            print(f"Comprimento do circulo {a}")
            continue
        case "4":
            break
        case _:
            print("Opção invalida.")
            continue