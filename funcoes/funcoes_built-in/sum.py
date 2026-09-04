#Sum:
#Funcao built-in
#Ela serve para somar os elementos de um iterável que contém números.
##Nao e possivel concatenar strings com o sum
#sum(iteravel)

# numeros = [10, 20, 30, 40] # 10+20+30+40 = 100
# resultado_da_soma = sum(numeros)
# print(resultado_da_soma)

# print(sum(range(1, 6)))
# #O range 1 a 6 faz 1, 2, 3, 4, 5
# #o sum soma isso e retorna 15

#O sum tambem possui um segundo argumento que e o valor inicial da soma
# numeros = [20, 30, 50]
# resultado = sum(numeros, 40)
# print(resultado)
##ou 
# print(sum(numeros, 40))
#O valor inicial da soma fica entao 40. 40+20+30+50 = 140
#Se o segundo argumento nao for definido, o inicio sera 0

notas = [15, 17, 14, 18]
media = sum(notas) / len(notas)
#media de notas o valor total 64 / 4 a quantidade de elementos
print(media) 
