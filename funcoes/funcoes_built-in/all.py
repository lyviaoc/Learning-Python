#All:
#Funcao built-in
##any() verifica se todos os elementos de uma coleção sao considerados True.
##sintaxe: all(iteravel)
#Sempre devolve um valor booleano: True ou False.

# numeros = [1, 2, 3, 4] #True
# print(all(numeros))

# numeros = [1, 2, 3, 0]
# print(all(numeros)) #False

numeros_menores_que_10 = [3, 5, 7, 10]
verificacao = all(n <= 10 for n in numeros_menores_que_10)
print(verificacao)

numeros_menores_que_10 = [3, 5, 7, 10]
verificacao = all(n >= 10 for n in numeros_menores_que_10)
print(verificacao)