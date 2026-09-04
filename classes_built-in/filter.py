#Filter:
#Chamada de classe built-in
#Deve receber uma funcao e uma lista
#Aplica a funcao a cada item apos realizar uma verificacao
#Serve para filtrar uma condicao especificada atraves de uma funcao (def ou lambda)
#Seleciona os elementos que passam numa condicao


#Ele faz uma verificacao, se der True vai para a lista nova se der False nao vai
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) #Apenas numeros pares vao para a lista nova
# print(numeros_pares)


# #Filtrando de todas as palavras nesta lista, apenas as que possuem a letra v
# palavras = ["Binóculo", 'Couve', "Vagem", "Tatu", "Barco"]
# palavras_com_v = list(filter(lambda x: "v" in x or "V" in x, palavras)) #Verifica se existe a letra v inserida em alguma das palavras da lista
# print(palavras_com_v)


#Exemplo com funcao def:
# def impares(x):
#  return x % 2 != 0

# def pares(x):
#  return x % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_pares = list(filter(pares, numeros))

# numeros_impares = list(filter(impares, numeros))

# print("Par ou impar?")
# escolha = input("Digite 1 para impar ou 2 para par:")
# if escolha == 1:
#     print(numeros_impares)
# else:
#     print(numeros_pares)



def letra_a(x):
    return "A" in x or "a" in x

comidas = ["Alho", "Alface", "Beterraba", "Noz", "Queijo"]
comidas_com_a = list(filter(letra_a, comidas))
print(comidas_com_a)