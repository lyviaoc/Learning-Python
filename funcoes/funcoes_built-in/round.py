#Round:
#Funcao built-in
#Usada para arredondar números.
#round(numero)

#Regra específica chamada round half to even ("arredondamento para o par mais próximo") quando o valor está exatamente no meio.
# print(round(4.5)) #=4 nao arredonda pois o proximo e impar
# print(round(4.6)) #=5 arredonda normal pois e acima da metade
# print(round(5.5)) #=6 par mais proximo

#É possivel escolher a quantidade de casas decimais desejadas
# round(numero, casas decimais)

numero = 3.66565654743
print(round(numero, 2))

