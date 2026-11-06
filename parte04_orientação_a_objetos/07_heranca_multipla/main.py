import os
from model import CarroVoador
def limpar():
    os.system("cls" if os.name == "nt" else "clear")
def main():
    carro_voador = CarroVoador(
        cambio=True,
        estepe=False,
        porta_malas=False,
        volante=True,
        retrovisor=True,
        buzina=True,
        escapamento=True,
        asa=True,
        turbina=True,
        aerofolio=True,
        cauda=True,
        manche=True,
        caixa_preta=True
    )
    limpar()
    print(f"cambio:{carro_voador.cambio}")
    print(f"cambio: {carro_voador.cambio}")
    print(f"estepe: {carro_voador.estepe}")
    print(f"porta malas: {carro_voador.porta_malas}")
    print(f"volante: {carro_voador.volante}")
    print(f"retrovisor: {carro_voador.retrovisor}")
    print(f"buzina: {carro_voador.buzina}")
    print(f"escapamento: {carro_voador.escapamento}")
    print(f"asa: {carro_voador.asa}")
    print(f"turbina: {carro_voador.turbina}")
    print(f"aerofólio: {carro_voador.aerofolio}")
    print(f"cauda: {carro_voador.cauda}")
    print(f"manche: {carro_voador.manche}")
    print(f"caixa preta: {carro_voador.caixa_preta}")

if __name__ == "__main__":
    main()