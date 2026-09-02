#COMO LER E ESCREVER ARQUIVOS COM PYTHON:

#MODO DE ESCRITA:
#a funcao precisa de dois argumentos obrigatórios, a localizacao do arquivo e o modo de abertura, se e apenas leitura ou escrita ou ambos..
#a variavel arquivo representa o arquivo dentro do py, apartir desta variavel serao realizadas as operacoes
#encoding utilizado para explicar o tipo de decodificacao uma vez que nao e aceito caracteres especiais como com acentos. o utf8 suporta acentuacoes
#O modo de abertura w e a cria um arquivo quando ele nao existe.
# with open("meus_arquivos/contatos.txt", "a", encoding="utf-8") as arquivo:
#     arquivo.write("Rogéria - 5432\n")
#     arquivo.write("Laura - 9212\n") #o "w" nao acrescenta ele substitui, por isso quando trocamos o nome do write ele nao escreve novamente ele substitui.
# #\n em python significa quebra de linha
# #somente oque esta escrito no bloco de codigo with pertence e funciona no arquivo

#MODO DE LEITURA:
# with open("meus_arquivos/contatos.txt", "r", encoding="-utf8") as arquivo:
#     nomes = arquivo.read()
#     print(nomes)

# with open("meus_arquivos/contatos.txt", "r", encoding="-utf8") as arquivo:
#     nomes = arquivo.readlines() #O readlines pega cada linha e coloca numa lista.
#     for nome in nomes:
#         print(nome)


#MODO DE LEITURA E ESCRITA:
#O r+ permite ler e escrever no arquivo
#O w+ e o a+ tambem permitem, porem para abrir um arquivo que nao existe ele cria
# with open("meus_arquivos/contatos.txt", "r+", encoding="-utf8") as arquivo:
#     nomes = arquivo.readlines() #O readlines pega cada linha e coloca numa lista.
#     for nome in nomes:
#         print(nome)
#     arquivo.write("Joana - 0897")


#SEEK:
# with open("meus_arquivos/contatos.txt", "w+", encoding="-utf8") as arquivo:
#     arquivo.write("Ana - 0909\n")
#     arquivo.seek(0) #Nao e possivel ler, apos o Ana ele nao consegue mais ler porque apos o cursor nao existe mais nada existe o espaco, e preciso usar o seek.
#     print(arquivo.read())