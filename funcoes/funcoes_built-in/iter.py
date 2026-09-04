#Iter:
## iter() é uma função built-in que recebe um iterável e devolve um iterador.
##É possivel visualizar cada valor de um iterador com (next(o iterador)).

lista = [10, 20, 30] #lista → iterável 

iterador = iter(lista) #iterador → iterador
print(next(iterador))
print(next(iterador))
print(next(iterador))
