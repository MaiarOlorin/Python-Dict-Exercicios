# Faça um programa que leia o nome e a 
# media de um aluno guardando tabem a 
# situação em um dicionario. No final 
# moste o conteudo da estrutura na tela.
nota = {}
nota["nome"]=input("Nome do aluno: ")
nota["media"]=int(input("Media do aluno: "))
if nota["media"] < 5:
    nota["situação"] = "REPROVADO"
if nota["media"] >= 5:
    nota["situação"] = "APROVADO"
for k, v in nota.items():
    print(f"{k} é igual a {v}")
