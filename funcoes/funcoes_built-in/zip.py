#Zip:
#Funcao built-in
#zip() junta elementos de dois ou mais iteráveis pela mesma posição.

# nomes = ["Ana", "João", "Maria"]
# idades = [15, 16, 17]

# for nome, idade in zip(nomes, idades):
#     print(nome, idade)


# nomes = ["Ana", "João", "Maria"]
# idades = [15, 16, 17]
# cidades = ["Faro", "Lisboa", "Porto"]

# for nome, idade, cidade in zip(nomes, idades, cidades):
#     print(nome, idade, cidade)


nomes = ["Ana", "João", "Maria"]
idades = [15, 16]
#Ana    → 15
#João   → 16
#Maria  → ???
for nome, idade in zip(nomes, idades):
    print(nome, idade)
#A Maria nao aparece. 3 elementos + 2 elementos = 2 pares. #Por padrão, zip() para quando o iterável mais curto acaba.

#Junta o primeiro elemento com o primeiro, o segundo com o segundo, o terceiro com o terceiro...