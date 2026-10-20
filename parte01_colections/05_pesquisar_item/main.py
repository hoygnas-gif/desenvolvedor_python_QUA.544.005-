# lista
cidade = [
    'Taguatinga',
    'Plano Piloto',
    'Santa Maria',
    'Gama',
    'Samambaia',
    'Santa Maria',
    'Taguatinga',
    'Planaltina',
    'Plano Piloto',
    'Brazlandia',
    'Plano Piloto',
]


# usuario informa o item a ser pesquisado
item = input("informe a cidade a ser pesquisada: ").strip(). title()

# verifica quantas vezes o termo foi encontrado na tela
print(f"{item} foi encontrado {cidade.count(item)} vezes na lista.")
