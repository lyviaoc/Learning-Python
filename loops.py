#Loops:
#Códigos que se repetem 
#while=enquanto

# contador = 10
# while contador >= 0: #Enquanto o contador for maior ou igual a zero:
#     print(f"A contagem atual é: {contador}") #Exiba o contador
#     contador-=1 #Faz parte do mesmo bloco de codigo #O contador é subtraido por 1 enquanto nao chega a zero

# senha = "Maldivas"
# tentativa_senha = "" #Guarda a tentativa do usuario de digitar a senha
# while senha != tentativa_senha: #Enquanto a senha for diferente da tentativa_senha mostrar "Digite a senha:"
#     tentativa_senha = input("Digite a senha:")
#     if senha != tentativa_senha:
#         print("Senha incorreta, tente novamente")
#     else:
#         print("Senha correta.") #Quando a senha é == a tentativa_senha, nao e mostrado mais "Digite a senha:"

# compras = ("Arroz", "Feijao", "Batata")
# for item in compras:
#     print(f"Compre: {item}")

# Numeros = [5, 6, 2, 9, 0, 8, 1]
# for numero in Numeros: #Para cada numero nos Numeros
#     if numero %2 == 0: #Se o numero for par  #Se nao entender "%" ir para conceitos
#         continue #Pula os numeros pares e vai para o proximo(no caso os impares)
#     print(numero) #Exibido:5,9,1
# continue #: Ir para o próximo

# Numeros = [5, 6, 2, 9, 0, 8, 1]
# for numero in Numeros: #Para cada numero nos Numeros
#     if numero %2 == 0: #Se o numero for par  #Se nao entender "%" ir para conceitos
#         break  #Para de exibir os Numeros quando encontra um numero par
#     print(numero)
# #break : Pausa/Para
