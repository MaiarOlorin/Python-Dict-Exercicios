pessoas = {"nome": "Israel", "sexo": "M", "idade": 22}

print (pessoas)
print("="*15)
print (pessoas["nome"])
print("="*15)
print (pessoas["idade"])
print("="*15)
print (pessoas.keys())
print("="*15)
print (pessoas.values())
print("="*15)
print (pessoas.items())
print("="*15)
print (f'O {pessoas ["nome"]} tem {pessoas ["idade"]} anos')

print("KEYS =====================================")
for k in pessoas.keys(): #keys mostra apenas a variavel do dicionario
    print(k)
print("ITEMS ====================================")
for i in pessoas.items(): #items mostra tanto a variavel e o conteudo
    print(i)
print("VALUES ====================================")
for v in pessoas.values(): #values mostra somente o conteudo do dicionario
    print(v)
print("ITEMS =======================================")
for k, v in pessoas.items():
    print(f"{k} = {v}")
print("="*15)

del pessoas["sexo"] # deleta elementos
print(pessoas.items())
print("="*15)
pessoas["peso"] = 76.4 #Adiciona elementos

for k, v in pessoas.items():
    print(f"{k} = {v}")
print("="*15)

brasil= list()
estado1 = {"UF":"Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "São paulo", "Sigla":"SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print(brasil[0])

print(brasil[0]["UF"])

print(brasil[1]["Sigla"])

r = ""