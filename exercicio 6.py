aproveitamento = dict()
gols = list()
totjog = list()
soma = 0
r = ""
while True:   
    aproveitamento["nome"] = input("Nome do Jogador: ")
    partida = int(input(f'Quantas Partidas {aproveitamento["nome"]} jogou? '))
    for c in range(0, partida):
        gol = int(input(f"Quantos gols na partida {c+1}? "))
        soma += gol
        gols.append(gol)

    aproveitamento["gols"] = gols[:]
    aproveitamento["total"] = soma
    totjog.append(aproveitamento.copy())
    aproveitamento.clear()
    gols.clear()
    soma = 0
    r = input("Continuar? [S/N] ")
    if r in "Nn":
        break
print("=="*30)
for c, v in enumerate(totjog):
    print(f'N°{c} = {totjog[c]["nome"]}. Gols por partida: {totjog[c]["gols"]}. Total de gols: {totjog[c]["total"]}')
print("=="*30)
aux = ""
while True:
    dados = int(input("Mostrar dados de qual jogador? "))
    print(f'levantamento do jogador {totjog[dados]["nome"]} ')
    for k, v in enumerate(totjog[dados]["gols"]):
        print(f'Na partida {k+1}, o jogador {totjog[dados]["nome"]} fez {v} gols')
    aux = input("Ver dados de outro jogador? [S/N]")
    if aux in "Nn":
        break
    
