#Colocando dicionarios em uma lista pelo teclado
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"]= str(input("UNIDADE FEDERATIVA: "))
    estado["sigla"]= str(input("SIGLA DO ESTADO: "))
    brasil.append(estado.copy()) #para copiar um dicionario é OBRIGATORIO ter o .copy()
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()

