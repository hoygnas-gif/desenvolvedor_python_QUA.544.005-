# biblioteca - equação de 2o grau diferente do 1o ela pode ter 2 raizes, assumindo 2 valores ao mesmo tempo

import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def eq_2o_grau(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta>0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        yield x1
        yield x2 
        
    elif delta == 0:
        x = -b/(2*a)
        yield x 

#yield - ela ao invés de finalizar a função, ele pausa a função e retomando de onde parou diferente return, que finaliza a função e retornar que finaliza e rotorna para inicio

    else:
        yield "Não existem Raizes reais"
    