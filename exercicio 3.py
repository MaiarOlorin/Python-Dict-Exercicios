# Crie um programa que leia nome, ano de 
# nascimento e carteira de trabalho e 
# cadestre-os (com idade) em um dicionario 
# se por acado a CTPS for difrente de ZERO 
# o docionario recebera tambem o ano de 
# contratação e o salario. calcule e 
# acrescente alem da idade quantos anos a 
# pessoa vai se aposentar.
# 35 anos de contribuição 
dados = {}
dados["nome"]=str(input("Nome: "))
dados["ano"]= str(input("Ano de nascimento: "))
dados["CTPS"]= int(input("Carteira de trablho [0] caso não tenha: "))

if dados["CTPS"] == 0:
    print(dados)
    for k, v in dados.items():
        print(f"O {k} tem valor {v}")

if dados["CTPS"] != 0:
    dados["contrato"]= int(input("Ano de contratação: "))
    dados["salario"]= int(input("Salario: "))

    c = dados["contrato"]
    ano_de_aposentadoria = c + 35
    aposentavel = ano_de_aposentadoria - 2022
    dados["aposentadoria"] = aposentavel
    print(dados)
    for k, v in dados.items():
        print(f"O {k} tem valor {v}")
