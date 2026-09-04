

# class Canal: #funcoes dentro de classes nao sao funcoes sao chamados metodos
#     def __init__(self, nome, descricao, inscritos): #funcao __init__ chama-se metodo construtor #o parametro self passa a representar a instancia canal_lyviaoc pois o metodo init foi chamado atraves do Canal
#         self.nome = nome
#         self.descricao = descricao
#         self.inscritos = inscritos

# canal_lyviaoc = Canal("LyviaOC", "Building myself into a backend engineer", 4)
# print(canal_lyviaoc) #Representacao do objeto que é uma mistura de propriedades e métodos.
# print(canal_lyviaoc.nome)
# print(canal_lyviaoc.descricao)
# print(canal_lyviaoc.inscritos)

# canal_lancode = Canal("LanCode", "Códigos e gatos", 34000)
# print(canal_lancode.nome, canal_lancode.descricao, canal_lancode.inscritos)


# class Pessoa: #Classe
#     def __init__(self, nome, idade): #Metodo init
#         self.nome = nome #self e objeto e .nome e atributo do objeto e nome e parametro
#         self.idade = idade

#     def apresentar(self): #Metodo apresentar que possui um comportamento
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# dados= Pessoa("Silvio Santos", 103) #dados é OBJETO / INSTÂNCIA
# dados.apresentar()



class NecessidadesGato():
    def beber_agua(self):
        print(f"{self.nome} está bebendo água.")
    def comer(self):
        print(f"{self.nome} está comendo.")
    def xixi_coco(self):
        print(f"{self.nome} está na caixa de areia.")
    def dormir(self):
        print(f"{self.nome} está dormindo.")

Safira = NecessidadesGato()
Safira.nome = "Safira"
Safira.beber_agua()


