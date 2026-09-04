#Enumerate:
#Funcao built-in
#enumerate() permite percorrer um iterável obtendo simultaneamente o índice e o valor de cada elemento.
#enumerate(iteravel)
#for indice, elemento in enumerate(iteravel) #dentro de um for


# frutas = ["Banana", "Morango", "Pera"]
# for indice, fruta in enumerate(frutas):
#     print(indice, fruta)
#indice, fruta = (0, "maçã") o Python pode separar esses dois valores
#indice → 0
#fruta  → "maçã"

#É possivel a enumeracao comecar a partir do numero que voce quiser. #Atraves do estabelecimento de um segundo argumento
# frutas = ["Banana", "Morango", "Pera"]
# for indice, fruta in enumerate(frutas, start=5):
#     print(indice, fruta)

# nome = "Python"
# for indice, letra in enumerate(nome, start=1):
#     print(indice, letra)

#O enumerate nao retorna listas sem o for
# frutas = ["maçã", "banana", "laranja"]
# resultado = enumerate(frutas)
# print(resultado)


#Sem enumerate:
# frutas = ["maçã", "banana", "laranja"]
# for i in range(len(frutas)):
#     print(i, frutas[i])

#Com enumerate:
frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(i, fruta)