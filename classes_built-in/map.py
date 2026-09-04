#Map:
#Chamada de classe built-in
#O Map deve receber uma funcao e uma lista. 
#O Map aplica a cada item da lista oque foi passado na funcao.
#Transforma cada elemento

#Era possivel usar o lambda e criar uma variavel e passar dentro do map mas com o lambda, e possivel criar o lambda dentro dos parametros/argumentos de uma funcao
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_multiplicados = map(lambda num : num * 2, numeros) #Dentro do map e preciso passar uma funcao e um iterador(que e uma lista) 
# for num in numeros:
#     print(num)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_multiplicados = list(map(lambda num : num * 2, numeros)) #o map foi aplicando em cada numero da lista
# print(numeros_multiplicados) #retorna outra lista com todos os itens com a funcao aplicada nele.


palavras = ["ornitorrinco", "otorrinolaringologista", "ovo", "ovov2"]
palavras_maiusculas = list(map(lambda string: string.upper(), palavras))
print(palavras_maiusculas)