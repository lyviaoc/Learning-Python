#Sorted:
#Funcao built-in
#Esta funcao serve para ordenar elementos, retornando uma nova lista.
#Sintaxe: sorted(iterable, key=None, reverse=False) ##O primeiro argumento e obrigatorio

# numeros = [5, 3, 1, 2, 4]
# ordenacao = sorted(numeros)
# print(ordenacao)

# numeros = [5, 3, 1, 2, 4]
# ordenacao = sorted(numeros, reverse=True)
# print(ordenacao)


#Parametro key=
#Responsavel por definir como a ordenacao deve ser feita, com base em que.

# nomes = ["Daniela", "Ana", "Joana", "Beatriz"]
# nomes_ordenados = sorted(nomes, key=lambda nomes: len(nomes))
# print(nomes_ordenados) #elementos com a mesma quantidade de caracteres continuam com a ordem inicial ex. "Daniela" e "Beatriz", como a "Daniela" ja estava antes do outro nome ela sera primeiro que o outro.

# nomes = ["Daniela", "Ana", "Joana", "Beatriz"]
# nomes_ordenados = sorted(nomes, key=lambda nomes: len(nomes), reverse=True)
# print(nomes_ordenados)

# NAO CONFUNDIR:
# .sort() e um metodo APENAS de listas
# .sort() modifica a lista e retorna none para a variavel criada enquanto a funcao sorted() cria uma nova lista e a lista original permanece sem alteracoes.

# numeros = [5, 2, 8, 1]
# resultado = numeros.sort()
# print(resultado) #Retorna none pois nao e criado nada dentro da variavel resultado
# print(numeros) #Retorna a lista alterada e ordenada por causa do .sort() que alterou a lista da variavel numeros
