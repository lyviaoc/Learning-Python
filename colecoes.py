#Coleções:
#Com colecoes as variaveis podem guardar mais de um valor.
#Colecoes sao estruturas de dados que permitem inserir varios valores/info dentro de uma variavel.
#Tipos principais de colecoes: Listas, Tuplas, Dicionarios e Set.
#É possivel transformar uma colecao em outra atraves de list(variavel em que a colecao esta armazenada) / tuple(variavel) / dict(variavel) / set(variavel)

#LISTAS(Mutaveis-podem ser alteradas):
#            0        1       2         #O primeiro valor é sempre zero
# frutas = ["Banana", "Maca", "Uva"]
# frutas[1] = "Abacaxi"  #[1] substitui o valor 1 pelo indicado. Neste caso o valor "Maca" é substituido por "Abacaxi".
# frutas.append ("Morango")  #.append adiciona o valor após o último valor da lista.
# frutas.insert (0,"Laranja")  #.insert usado para inserir o valor onde desejado. Especificar se é 0,1, 2.. acompanhado da virgula apos o numero e o valor apos a virgula.
# frutas.remove ("Uva")  #.remove utilizado para remover algum valor da lista
# if "Uva" in frutas:
#     print("Tem uva nas frutas.")
# else:
#     print("Nao tem uva nas frutas.")
##print(frutas[1])
##exibe:"Abacaxi"
#Através destes códigos é possível alterar listas sem alterar seu próprio código


#TUPLAS(Imutaveis-nao podem ser alteradas):
# cores = ("Vermelho", "Verde", "Azul") #Utiliza-se parenteses
# print(cores)
#É possível colocar tupla dentro de tupla e lista dentro de lista através de uma lista
#Exemplo de lista que contem tuplas:
#                         0                      1                     2
# minhas_tuplas = [("Banana", "Pessego"), ("Cachorro", "Gato"), ("Verde", "Amarelo")]
#                     0          1             0          1         0         1   
# print(minhas_tuplas[2][0]) #exibe: "Verde"

#Exemplo de lista que contem listas:
# minhas_listas = [["Abacaxi", "Morango"], ["Girassól", "Rosa"]]
# print(minhas_listas[1][1])

#Exemplo de tupla que contem tuplas:
# tuplinhas = (("Mario Kart", "Minecraft"), ("Zelda", "FNAF"))
# print(tuplinhas[0][1])

#Exemplo de tupla que contém listas:
# listinhas = (["Feijao", "Batata", "Arroz"], ["Cocada", "Sorvete", "Doce de Leite"])
# print(listinhas[1][2])
#É possível listas conterem tuplas, listas conterem listas, tuplas conterem tuplas e tuplas conterem listas


#DICIONARIOS(Mutaveis-podem ser alterados):
#Estrutura de dados onde voce vai nomear os valores
# dados = {"nome":"Quinn", "idade":29} #É utilizado chaves.
# dados["idade"] = 30 #Colchetes e renomeia o valor porque e como se fosse o numero escolhido para renomear ex: [1]
# print(dados["idade"]) #É possível buscar valores como um dicionario 
# print(dados["nome"]) 
##Nao usa indice porem e possivel alterar os valores atribuidos a outros valores dentro do dicionario


#SET(Mutaveis-podem ser alterados):
#Um set é uma coleção que guarda valores únicos.
#É utilizado chaves.

# numeros = {1, 2, 2, 3, 3, 3} #Se repetirmos valores as repeticoes sao eliminadas
# print(numeros)

#Transformar lista em set para remover nomes repetidos. set(variavel)
# nomes = ["Ana", "João", "Ana", "Pedro", "João"]
# nomes_unicos = set(nomes)
# print(nomes_unicos)

#Verificar se realmente existe determinado valor no set
# frutinhas = {"Banana", "Laranja", "Pera"}
# print("Banana" in frutinhas) #É exibido: True
# print("Melancia" in frutinhas) #É exibido: False

#Adicionar e remover valores ##Nao e possivel alterar um valor diretamente porque o set nao tem indice (O indice e a posicao de cada valor, por exemplo em python e localizado a posicao a partir do 0. tipo 0  1  2..)
# numeros = {1, 2, 3}
# numeros.add(5)
# numeros.remove(3)
# print(numeros)

#Uniao todos os elementos de a e b
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)
#Intersecao elementos que existem em ambos
# print(a & b)

#Diferenca elementos que estao em a mas nao estao em b 
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a - b)
# #elementos que estao em b mas nao estao em a
# print(b - a)

#Cuidados
##Um set e criado com chaves porem:
# empty = {} #Isto e um dicionario vazio
# empty = set() #ISTO e um set vazio