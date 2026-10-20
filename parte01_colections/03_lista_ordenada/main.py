# lista de cidades
cidades = ["Rio deJaneiro" , "Brasilia" , "São Paulo" , "Goiania" , "Cuiaba"]

" ordena a lista"
cidades.sort()

# exiba a lista en ordem alfabética
for cidade in cidades:
    print(cidade)

    # reverte a lista
    cidades.sort(reverse=True)

    # exibe a lista em ordem reversa
    for cidade in cidades:
        print(cidade)