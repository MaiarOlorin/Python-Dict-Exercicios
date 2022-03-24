# Crie um programa onde 4 jogadores jogue 
# um dado e tenham resultados aleatorios. 
# guarde esses resultados em um dicionario. 
# no final coloque esse dicionario em 
# ordem sabendo que o vencedor tirou o 
# maior numero.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = list()
for c in range(1, 5):
    jogo[f"Jogador {c}"] = randint(1, 6)
print("Valores sorteador: ")
for k, v in jogo.items():
    print(f"O {k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}.")

