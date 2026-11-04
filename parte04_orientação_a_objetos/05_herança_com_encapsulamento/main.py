#SECTION - Biblioteca
import os
from model import PessoaFisica, PessoaJuridica

#SECTION - Limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    #SECTION - Instanciamento
    usuario = PessoaFisica(
        nome="",
        cpf="",
        telefone="",
        email="",
    )
    #NOTE - Outras formar de Instanciamento
    empresas = PessoaJuridica(nome_fantasia="",razao_social="",cnpj="",telefone="",email="")

#SECTION - Entrada de Usuario
    print(f'{"-" * 20} Insira os Dados do usuário {"-" * 20}')                            
    usuario.nome = input("Informeo seu Nome:{usuario.nome} ").strip().title()
    usuario.cpf = input("Informeo seu cpf:{usuario.cpf} ").strip()
    usuario.telefone = input("Informeo seu telefone:{usuario.telefone} ").strip()
    usuario.email = input("Informeo seu email:{usuario.email} ").strip().lower()
    limpar()
 
 #SECTION - Entrada empresa
    print(f"{"-"*20}Insira os Dados da Empresa {"-"*20}")  
    usuario.nome_fantasia = input("Informeo seu nome fantasia: ").strip().title()
    usuario.razao_social = input("Informeo seu razao social: ").strip()
    usuario.cnpj = input("Informeo seu CNPJ: ").strip()
    usuario.telefone = input("Informeo seu telefone: ").strip().lower()
    usuario.email= input("Informeo seu email: ").strip().lower()
    limpar()

#SECTION - Saída usuario
    print(f"{"-"*20} Dados do usuario {"-"*20}")
    print(f"O seu Nome é {usuario.nome}")
    print(f"O seu CPF é {usuario.cpf}")
    print(f"O seu Telefone é {usuario.telefone}")
    print(f"O seu email é {usuario.email}"  )

    #SECTION - Saia da Empresa
    print(f"{"-"*20} Dados da empresa {"-"*20}")
    print(f"O seu Nome Fantasia é {empresas.nome_fantasia}")
    print(f"O seu Razão Social é {empresas.razao_social}")
    print(f"O seu CNPJ é {empresas.cnpj}")
    print(f"O seu Telefone é {empresas.cnpj}")
    print(f"O seu email é {empresas.email}")

#SECTION - Rodar
if__name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)