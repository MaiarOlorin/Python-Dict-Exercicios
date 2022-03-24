aproveitamento = dict()
gols = list()
soma = 0
aproveitamento["nome"] = input("Nome do Jogador: ")
partida = int(input(f'Quantas Partidas {aproveitamento["nome"]} jogou? '))
for c in range(0, partida):
    gol = int(input(f"Quantos gols na partida {c+1}? "))
    soma += gol
    gols.append(gol)
aproveitamento["gols"] = gols
aproveitamento["total"] = soma
print(aproveitamento)
for k, v in aproveitamento.items():
    print(f"O campo {k} tem valor {v}")
print(f'O jogador {aproveitamento["nome"]} jogou {partida}.')
for v, c in enumerate(gols):
    print(f"Na partida {v+1}, fez {c} gols")

