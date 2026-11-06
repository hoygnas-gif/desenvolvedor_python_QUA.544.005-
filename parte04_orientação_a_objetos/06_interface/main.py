
# bibliotecas
import os
import random

from model import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # instancia a classe Conta
    cc = Conta(
        titular="",
        cpf="",
        agencia="1010-1",
        n_conta=f"{random.randint(10000, 99999)}-1",
        saldo=0.0
    )
    # Cadastro do titular
    cc.title = input("Digite o nome do titular da conta: ").strip().title()


    cc.cpf = input("Digite o CPF do titular da conta: ").strip()
    limpar()
# Menu bancário
    while True:
        print("\n--- MENU BANCÁRIO ---")
        print("1 - Consultar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                print("Encerrando o programa...")
                break

            case "1":
                cc.consultar_conta()
                continue

            case "2":
                valor = float(
                    input("Informe o valor do depósito: R$ ")
                    .replace(",", ".")
                )
                saldo = cc.depositar(valor)
                limpar()
                print(
                    f"Depósito efetuado. Saldo: R$ {saldo:.2f}"
                )
                continue

            case "3":
                valor = float(
                    input("Informe o valor de saque: R$ ")
                    .replace(",", ".")
                )

                if 0 < valor <= cc.saldo:
                    saldo = cc.sacar(valor)
                    limpar()
                    print(
                        f"Saque efetuado com sucesso. "
                        f"Saldo atual: R$ {cc.saldo:.2f}"
                    )
                else:
                    print("Não foi possível efetuar o saque.")

                continue

            case _:
                print("Opção inválida.")
                continue
if __name__ == "__main__":
        main()
