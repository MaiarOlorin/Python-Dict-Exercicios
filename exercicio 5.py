# Crie um programa que leia nome, sexo e 
# idade de varias pessoas, guardado tudo 
# um em um dicionario e todos os dicionarios 
# em um lista. no final moste: 
# (a) quantas pessoas foram cadastradas 
# (b) a media de idade de todos 
# (c) uma lista com todas as mulheres 
# (d) uma lista com todas as idades acima da media 
cadastro = list()
mulheres = list()
mul = list()
pessoas = dict()
totidade = 0
r = ""
cont = 0
while True:
    pessoas["nome"] = input("Nome: ")
    sexo = str(input("Sexo:[M/F] "))
    pessoas["sexo"] = sexo
    idade = int(input("Idade: "))
    pessoas["idade"] = idade
    totidade += idade
    if sexo in "Ff":
        mul.append(pessoas["nome"])
        mulheres.append(mul[:])
        mul.clear()

    cadastro.append(pessoas.copy())
    pessoas.clear()
    r = input("Quer continaur? [S/N] ")
    cont += 1
    if r in "Nn":
        break
media = totidade / 2

print(f"Total de pessoas cadastradas {cont}")
print(f"Media de idade é de {media}")
print(f"Mulheres cadastradas foram:")
for c, v in enumerate(mulheres):
    print(v)
print("Pessoas com idade acima da média geral:")
for k, v in enumerate(cadastro):
    if cadastro[k]["idade"] > media:
        print(v)