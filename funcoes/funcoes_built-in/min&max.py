#Min e Max:
#Funcoes built-in
#min() significa minimum e serve para encontrar o menor valor de um conjunto de valores.
#max() significa maximum e faz o contrário: procura o maior valor.

#O min e max podem receber um iteravel min(iteravel) max(iteravel)
# numeros = [10, 5, 20, 3, 15] 
# resultado = min(numeros) 
# resultadov2 = max(numeros)

# print(resultado)
# print(resultadov2)

# minimo = min(range(1,11))
# maximo= max(range(1,11))
# print(minimo)
# print(maximo)

#É possivel passar argumentos ao inves de iteraveis
# yup = min(23, 47, 22, 21, 100)
# yo = max(23, 47, 22, 21, 100)
# print(yup)
# print(yo)

strings = ["Bola", "Arpao", "Carro"]
print(min(strings))
print(max(strings))
#min() → encontra o elemento que vem primeiro na ordem lexicográfica. por exemplo entre a c e j ele encontra o a
#max() → encontra o elemento que vem depois na ordem lexicográfica. ex: entre a c e j ele encontra o j