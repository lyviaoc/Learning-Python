##Reversed:
#Funcao built-in
#A funcao reversed recebe um objeto e permite percorrê-lo do último elemento para o primeiro.
#Retorna objetos do tipo reverse. 
#sintaxe: reversed(colecao)
#Nao e criada uma nova lista, e criado um iterador que sabe como acessar os elementos de trás para frente.

# nomes = ("Thiago", "Francisca", "Ana")
# for n in reversed(nomes): #O reversed nao altera a lista original. Ele cria um objeto do tipo reversed que e um iterador ou seja pode ser percorrido. Por isso e utilizado o loop for
#     print(n)
# #Se realmente quissese transformar em lista:
# lista_invertida = list(reversed(nomes))
# print(lista_invertida)
#Com a funcao reversed() a colecao original continua igual

#(so serve para listas) Já com o metodo de list: .reverse() 
nomes = ["Ana", "João", "Maria"]
resultado = nomes.reverse()

print(nomes) #Maria, Joao, Ana
print(resultado) #None

#Funciona com outras colecoes porem existem algumas regras.
#Com uma string:
palavra = "Python"
print("".join(reversed(palavra)))