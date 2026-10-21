 # tupla
dias_da_semana = (
    "Domingo",
    "Segunta-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sabado"
)
print("")

# exibe a tupla
for dia in dias_da_semana:
    print(dia)

print("")

#NOTE: se tentar alterar a tupla, o programa da erro. Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possivel ordenar. {e}.")
finally:print("Programa encerra")