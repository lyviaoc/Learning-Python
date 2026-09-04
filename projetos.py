##ESQUEMA DE APOSTA
# import random
# import time

# n_possiveis = range(1,100)
# esquema_hehe = list(filter(lambda x: x % 2 != 0, n_possiveis))
# aleatoriedade_hehe = random.choice(esquema_hehe)


# resposta = input("Bem vindo a Casa de Apostas Pares. Gostaria de apostar em um numero par?(preco entradinha:50$) (Y/N?)")
# if resposta == "Y" or resposta == "y":
#     print("Amável. Aguarde preciosos 10 segundos e a roleta de numeros de 1 a 100 irá girar. Se o numero for par voce ira ganhar uma quantia generosa (5000$ no cash bb).")
#     time.sleep(10)
#     print(aleatoriedade_hehe)
#     print("Carambolas! Nao foi desta vez.")
# elif resposta == "N" or resposta == "n":
#     print("Son of a bad mother! >:C")
##Projetinho zoas



#MEDIA DE NOTAS MATEMATICA

# from decimal import Decimal, ROUND_HALF_UP
# print("Vamos calcular a sua média em matemática e verificar se está aprovado, reprovado ou de recuperação!")

# while True:
#     try: 
#         prova1 = Decimal(input("Qual a sua nota da prova de algebra? ").replace(",", "."))
#         if prova1 > 10 or prova1 < 0:
#             raise Exception
#         prova2 = Decimal(input("Qual a sua nota da prova de geometria? ").replace(",", "."))
#         if prova2 > 10 or prova1 < 0:
#             raise Exception
#         prova3 = Decimal(input("Qual e sua nota da prova de estatistica e dados? ").replace(",", "."))
#         if prova3 > 10 or prova1 < 0:
#             raise Exception
#         notas_provas = [prova1, prova2, prova3]
#         somatorio_provas = sum(notas_provas)
#         quantidade_provas = len(notas_provas)
#         media = somatorio_provas / quantidade_provas
#         media_arredondada = media.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        
#         if media_arredondada >= 6:
#             print(f"Aprovado! Sua média é: {media_arredondada}")
#         elif media_arredondada == 5:
#             print(f"Recuperação! Sua média é: {media_arredondada}")
#         else:
#             print(f"Reprovado! Sua média é {media_arredondada}")
#         break
#     except ValueError, Exception:
#         print("Digite uma nota válida!!")
##Review: logica no geral boa mas durante o tratamento de erros esqueci de tratar erros que nao sao considerados erros pelo python. Tratei do ValueError mas nao de erros como o usuario digitar um numero maior que 10, uma vez que o numero maximo de uma prova e 10. Também nao corrigi se caso o usuario digitasse um numero negativo.
##Os nomes das minhas variaveis antes das alteracoes poderiam estar mais bem representados.
##Novos aprendizados: o float e um numero flutuante e quebra um galho para utilizar quando queremos trabalhar numeros com casas decimais. Entretanto, ele nao e tao preciso quanto a biblioteca decimal que possui o Decimal que e feita exatamente para precisao de numeros decimais. O Decimal e uma classe que pode definir Decimal()
##Escrevi dois elif sem necessidade o ultimo apenas else facilita tempo e faz mais sentido.




class Data:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def cumprimento(self):
         print(f"Olá, {self.nome}! Voce tem {self.idade} anos e seu sexo é {self.sexo}.")

print("Preencha os dados requisitados do formulário.")
while True:
    try:
        nome = input("Qual é o seu primeiro nome? ")
        if len(nome) > 20 or len(nome) < 3 or nome == "": raise Exception

        print("Caracteres nao sao suportados. Digite apenas numeros:")
        idade = int(input("Qual é a sua idade? "))
        if idade < 0 or idade <= 5 or idade > 105: raise Exception

        sexo = input("Qual é o seu sexo? ").lower()
        if sexo not in ("feminino", "masculino"): raise Exception
        
        dados = Data(nome, idade, sexo)
        dados.cumprimento()
        break
    except ValueError, Exception:
        print("Preencha o formulario corretamente.")


# class Pessoa: #Classe
#     def __init__(self, nome, idade): #Metodo init
#         self.nome = nome #self e objeto e .nome e atributo do objeto e nome é parametro
#         self.idade = idade

#     def apresentar(self): #Metodo apresentar que possui um comportamento
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# dados= Pessoa("Silvio Santos", 103) #dados é OBJETO / INSTÂNCIA
# dados.apresentar()