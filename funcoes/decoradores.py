#Decoradores:
#É possivel alterar o comportamento de funcoes criando e usando decoradores
#É querer adicionar algum comportamento a uma funcao sem modificar a funcao original.

#Criar uma funcao nova por cima da original e retorna-la 
# def meu_decorador(func):
#     print("Sou um decorador!")

#     func()

# @meu_decorador
# def bom_dia():
#     print("Bom dia!")

# def meu_decorador(func): #2.2a funcao meu_decorador precisa ter a funcao(que e considerada argumento) que vai decorar no caso a func que corresponde a funcao bom_dia
#     def wrapper(): #a funcao wrapper e criada por cima da funcao bom_dia #2-a funcao wrapper faz: 
#         print(f"Vou executar a funcao {func.__name__}") #3-printa isso aqui

#         func() #4-executa a funcao que esta sendo decorada(no caso a funcao bom_dia)

#         print(f"Executei a funcao {func.__name__}") #5-printa isso aqui
#     return wrapper #6-retorna a funcao wrapper (porque e como se ela estivesse fora da funcao entao retorna a funcao uma vez que oque tem dentro dela e escopo local(Tudo que e usado dentro da funcao so pode ser usado dentro da funcao))

# @meu_decorador #1.1-Colocamos a funcao meu_decorador para decorar a funcao bom_dia #1-Quando usamos o @meu_decorador ele fez a funcao wrapper
# def bom_dia():
#     print("Bom dia!")

# bom_dia()


# from time import sleep, time

# def contador(func): 
#     def wrapper():  #com a funcao wrapper dentro da funcao decoradora e possivel criar oque quisermos por cima da funcao bom_dia
#         inicio = time() #Atribuimos a biblioteca time como valor da nossa variavel #inicio e quando abrimos o terminal

#         func() 

#         fim = time()  #fim apos a funcao bom_dia ser executada

#         segundos = fim - inicio #O tempo de execucao e o fim que foi apos 3s e o inicio em 0s
#         print(f"A funcao {func.__name__} levou {segundos:.2f} segundos para ser executada") # :.2f especifica a quantidade de casas decimais que o float deve ter desta forma e exibido 3.00 sem a especificacao oque seria exibido seria 3.00104.. se quisessemos 1 casa :.1f 3.0 e sem casas :.0f 3


#     return wrapper #retorne a funcao

# @contador        #A funcao contador vai decorar a funcao bom_dia
# def bom_dia():  
#     sleep(3)     #a biblioteca sleep nao exibe nada ate a quantidade de segundos escolhida acabar
#     print("Bom dia!")

# bom_dia()



# def meu_decorador(mensagem): #Gerador de decoradores #O decorador agora possui um parametro chamado mensagem

#     def novo_decorador(func): #Criou o real decorador: 

#         def wrapper(): #Que criou a funcao wrapper que decora(cria coisas por cima da)/a funcao bom_dia

#             print("Vou executar a sua funcao.") #Que exibe os prints e o parametro mensagem
#             print(f"Mensagem recebida: {mensagem}")
#             func()
#             print("Executei a sua funcao.")

#         return wrapper #retorna a funcao wrapper
#     return novo_decorador #retorna a funcao decoradora

# @meu_decorador('Safirinha linda!') # A string "Safirinha linda!" esta sendo passada para a funcao meu_decorador
# def bom_dia():       
#     print("Bom dia!")

# bom_dia()


# def meu_decorador(func):
#     def wrapper(*args, **kwargs): #os args sao os argumentos nao especificados que sao exibidos como tuplas: (3,). e os kwargs que sao os argumentos especificados por exemplo b=2 que sao exibidos como dicionarios:{"b": 2}
#         print(args)
#         print(kwargs)        
#     return wrapper

# @meu_decorador
# def somar(a, b):
#     return a + b

# somar(3, b=2)


# def meu_decorador(func):
#     def wrapper(*args, **kwargs):#1 #é uma maneira de dizer, wrapper, aceite quaisquer argumentos que a funcao original receber #O args e o kwargs consegue lidar com praticamente qualquer quantidade e combinacao de argumentos
#         print(f"Vou executar a sua funcao {func.__name__}")
#         return func(*args, **kwargs)#2 #é uma maneira de dizer, agora passa esses mesmos argumentos para a funcao original #É preciso dos asteristicos para a chamada da funcao mas quando e print nao tem necessidade. 
#     return wrapper

# @meu_decorador
# def somar(a, b):
#     return a + b

# resultado = somar(a=3, b=2) #O args e o kwargs serviram para a funcao localizar os argumentos. 1 Colocamos o args e o kwargs como argumentos da funcao wrapper. Porém, 2 devemos colocar o args e kwargs dentro da func que esta dentro da funcao wrapper tambem pq se nao e apenas retornado o wrapper e nao e retornado a func que representa a nossa funcao original somar. Isto e feito porque serao exibidos o decorador e a nossa funcao, e o decorador esta por cima da funcao entao o decorador tambem deve estar de acordo com a funcao.
# print(resultado) #A soma so consegue ser realilizada pois a funcao encontra os argumentos a corresponde a 3 e b corresponde a 2, gracas ao args e kwargs. O python entende que aqueles argumentos foram especificados e sao considerados como kwargs.




def decorador_s(func):
    def wrapper():
        print("Oque a Safira é?")

        func()

        print("fofinha<3")
    return wrapper



@decorador_s
def safirinha():
    print("A Safira é:")

safirinha()