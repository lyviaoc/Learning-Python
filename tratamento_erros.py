#Tratamento de erros:
#Trata erros. #Se uma sequencia de codigos for executada e der algum erro ele para e comeca a executar um outro codigo criado para se caso aquele erro acontecesse.
#Documentacao de todas as classes de erros disponiveis python https://docs.python.org/3/library/exceptions.html#concrete-exceptions
# try:
#     n1 = int(input("Digite um numero:"))
#     n2 = int(input("Digite outro numero:"))
#     resultado_soma = n1 + n2
#     print(f"{n1} + {n2} = {resultado_soma}")
# except Exception as error:
#     print(error)
#     print("Digite um numero válido!")


# try:
#     numero = float(input("Digite um número:"))
#     resultado = 10 / numero
#     print(f"O resultado é {resultado}")
# except ValueError as error:
#     print(f"Digite um numero válido. {error}")
# except ZeroDivisionError as erro:
#     print(f"Nao e possivel dividir por 0. {erro}")


# try:
#     lista_top = ["Brocolis", "Beterraba", "Goiaba"]
#     print(lista_top[3])
# except IndexError as erro:
#     print("Índice incorreto.")


# try: #Tente:
#     print("Divisao por 10.")
#     numero = float(input("Digite um número:"))
#     resultado = 10 / numero
# except ValueError as error: #Excecao se der a classe de erro ValueError printa:
#     print(f"Digite um numero válido. {error}") #{error} mostra qual o tipo de erro ocorreu
# except ZeroDivisionError as erro: 
#     print(f"Nao e possivel dividir por 0. {erro}")
# else:   #Se nao houver erros printa:
#     print(f"O resultado é {resultado}")
# finally: #O finally vai rodar de qualquer maneira
#     print("Fim do cálculo.")


#o RAISE cria erros personalizados para casos especificos, ou seja, e possivel criar seus proprios erros.
# try:
#     idade = int(input("Digite a sua idade:"))
#     if idade < 0: #Se a idade inserida for negativa
#         raise Exception("Digite uma idade válida.") #Raise e lancar um erro/excecao
#     elif idade > 120: #Se a idade for maior do que 120(anos)
#         raise Exception("Digite uma idade válida") #raise Exception ="Crie/lance uma excecao". a excecao/Exception é o valor dentro dos parenteses
# except Exception as erro: #Todo erro vai ser capturado com a classe Exception #O Exception esta sendo atribuido a váriavel erro e os valores das Exception criadas anteriormente irao aparecer quando a variavel for chamada.
#     print(f"Erro: {erro}") #Será exibido oque esta dentro da variavel erro, ou seja as Exception criadas pelo raise 
# else:
#     print(f"Sua idade é: {idade}") #Caso contrario se nao houver erros.
# #Neste codigo foi necessario criar erros para impedir usuarios de colocarem idades inexistentes porem que ainda assim atendem os requisitos da classe integer, rodando sem dar erro no proprio terminal.


# try:
#     def ola(nome):
#         print(f"Olá {nome}")
#     nome_pessoa = (input("Qual é o seu nome?")) #Tudo digitado é considerado str no input
#     if nome_pessoa.isdigit: #.isdigit verifica se os caracteres da string sao numeros
#         raise Exception
#     ola(nome_pessoa)
# except Exception as erro:
#     print("Digite um nome válido.")

    