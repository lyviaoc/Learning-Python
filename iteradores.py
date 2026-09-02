#Iterável:
#Se um objeto pode ser usado diretamente num loop for, ele é iterável.
#Um iterável é um objeto que pode ser percorrido elemento por elemento.
#Os iteráveis podem ser usados com o for
#Servem para guardar dados que queremos percorrer
#list
#tuple
#str
#set
#dict
#range 


# lista = [10, 20, 30]
# tupla = (10, 20, 30)
# texto = "Python"
# set = {10, 20, 30}
# dicionario = {"a": 1, "b": 2}


#Iterador: 
#Um iterador é um objeto que permite obter os elementos de um iterável um por um, através de next().
#Todo iterador é iterável, mas nem todo iterável é um iterador.
#Eu preciso utilizar o iter em uma variavel iteravel gerando um iterador para obter cada elemento do iteravel um por um atraves do next. Nao e possivel usar o next diretamente em um iteravel e preciso de um iterador. Desta forma quando quiser saber qual e o proximo valor de um iteravel um de cada vez utiliza-se o next

lista = [10, 20, 30] #lista → iterável 

iterador = iter(lista) #iterador → iterador
print(next(iterador))
print(next(iterador))
print(next(iterador))


