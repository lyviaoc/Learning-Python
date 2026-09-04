#Funcoes:
# #Organizam codigo
# def ola(nome):  #A funcao criada esta pedindo o argumento nome que tera de ser atribuido quando a funcao for chamada
#     print(f"Olá, {nome}") #Quando a funcao for chamada é isso que sera exibido

# nome_inserido = input("Qual é o seu nome?")
# ola(nome_inserido) #Chamou a funcao e a variavel nome_inserido vai para o argumento nome

# def somar(n1, n2): #Primeiro os argumentos sao apresentados
#     resultado = n1 + n2 #É criada a váriavel resultado que soma os argumentos
#     return resultado #Return retorna o valor da variavel resultado
# resultado_da_soma = somar(2, 3) #A nova variavel criada vai chamar a funcao somar com os argumentos atribuidos a ela e oque estiver no return vai ir para a variavel que esta recebendo a funcao (no caso a variavel resultado_da_soma)
# print(f"Resultado: {resultado_da_soma}") #Exibindo a soma


# def listas(valor1, valor2):
#     minhas_listas = [valor1, valor2]
#     return minhas_listas    #ESCOPO/ESCOPO LOCAL tudo que esta sendo usado dentro da funcao so pode ser usado dentro da funcao (no caso a variavel minhas_listas so e reconhecida dentro do bloco de codigo da funcao)
# lista = listas("Banana", "Couve")
# lista[0] = "Alface"
# print(f"Oque precisa comprar: {lista}")


# def listas():
#     lista = input("Oque falta na lista de compras?")
#     return lista
# minha_lista = listas()
# print(f"Para comprar: {minha_lista}")


# def yay():
#     print(nome)
# nome = "Lyvinha"
# yay()

# nome = "Lyvinha" #a variavel nome esta no ESCOPO GLOBAL -apesar da variavel nome estar fora da funcao, ela ainda consegue ser utilizada dentro dela(da funcao)
# def yay():
#     print(nome)
# yay()
#O Escopo global, ao contrario do Escopo local, (Tudo que e usado dentro da funcao so pode ser usado dentro da funcao) é possivel usar oque esta fora da funcao dentro da funcao

# def sominha(n1, n2):
#     result = n1 + n2
#     return result

# def cumprimento(nome):
#     print(f"Olá, {nome}.")


# n1 = int(input("Digite um número:"))
# n2 = int(input("Digite outro número:"))
# def multiplicacao(n1, n2):
#     m = n1 * n2
#     return m
# resultado = multiplicacao(n1, n2)
# print(f"O resultado da multiplicacao é {resultado}")


#Yield:
#yield é uma palavra-chave usada para criar funcoes geradoras que produzem generators e produzir valores um de cada vez, pausando a execução da função entre cada valor. #yield e como um return que não termina a função. e deixa aberta para futuras alteracoes
# def contar_ate_5():
#     for i in range(1, 6):
#         yield i #Aqui o yield permite produzir um número de cada vez, em vez de criar uma lista com todos os números.

# for numero in contar_ate_5():
#     print(numero)


# def exemplo():
#     print("Começou")
#     yield 10 #o yield produziu estes valores

#     print("Continuou")
#     yield 20

#     print("Terminou")

# x = exemplo()

# while True:
#     try:
#         print(next(x))
#     except StopIteration:  #Quando nao ha mais elementos ele aparece o erro StopIteration
#         break