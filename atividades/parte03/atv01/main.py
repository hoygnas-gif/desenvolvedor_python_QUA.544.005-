# TODO: parte 03 atividade 01
'''
Crie um programa que calcule o peso de uma pessoa
em um planeta do sistema solar escolhido por ela.
'''

# Biblioteca
from modulo import limpar, peso_astro


def main():

    # Dicionário com a gravidade dos astros
    astros = {
        'mercurio': 3.73,
        'venus': 8.73,
        'terra': 9.8,
        'lua': 1.62,
        'marte': 3.73,
        'jupiter': 24.92,
        'saturno': 10.5,
        'urano': 8.73,
        'netuno': 11.77
    }

    limpar()

    # Entrada de dados
    massa = float(input(
        "Informe sua massa em kg: "
    ).replace(",", "."))

    print("\n=== ASTROS DISPONÍVEIS ===")

    # Exibir os astros
    for chave in astros:
        print(chave.upper())

    # Escolha do usuário
    escolha = input(
        "\nEscolha um astro: "
    ).lower().strip()

    # Verificar se o astro existe
    if escolha in astros:

        gravidade = astros[escolha]

        peso = peso_astro(massa, gravidade)

        print("\n=== RESULTADO ===")
        print(f"Astro: {escolha.upper()}")
        print(f"Gravidade: {gravidade} m/s²")
        print(f"Peso: {peso:.2f} N")

    else:
        print("Astro não encontrado!")


if __name__ == "__main__":
    main()