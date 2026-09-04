#Any:
#Funcao built-in
#any() verifica se pelo menos um elemento de uma coleção é considerado True.
#sintaxe: any(iteravel)
#Sempre devolve um valor booleano: True ou False.

# numeros = [0, 0, 0]
# print(any(numeros)) #False

# numeros = [0, 9, 5]
# print(any(numeros)) #True

# nomes = ["", "", ""]

# print(any(nomes)) #False

# nomes = ["", "", "Ana"]

# print(any(nomes)) #True


numeros_maiores_que_20 = [21, 23, 47, 31]
teste = any(n < 20 for n in numeros_maiores_que_20)
print(teste)
