#Isinstance:
#Verifica se um objeto pertence a determinado tipo/classe.
#Funcao built-in
#Sintaxe:isinstance(objeto, tipo)
#Sempre devolve um valor booleano: True ou False.

# idade = 15
# idadev2 = [15]
# print(isinstance(idade, int)) #True
# print(isinstance(idadev2, int)) #False
# print(isinstance(idadev2, list)) #True

valor = 3.5
print(isinstance(valor, (int, float))) #e possivel atraves de uma tupla verificar mais de uma classe 'e int ou float?' #True

# valor = input("Digite um número: ")
# if isinstance(valor, str):
#     print("Você digitou uma string") #True