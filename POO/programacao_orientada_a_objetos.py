#PROGRAMACAO ORIENTADA A OBJETOS:

# class Canal: #funcoes dentro de classes nao sao funcoes sao chamados metodos
#     def __init__(self, nome, descricao, inscritos): #funcao __init__ chama-se metodo construtor #o parametro self passa a representar a instancia canal_lyviaoc e canal_lancode pois o metodo init foi chamado atraves do Canal
#         self.nome = nome
#         self.descricao = descricao
#         self.inscritos = inscritos

#     def inscrever(self, quantidade=1):
#         self.inscritos += quantidade
# ##
# canal_lyviaoc = Canal("LyviaOC", "Building myself into a backend engineer", 4)
# print(canal_lyviaoc) #Representacao do objeto que é uma mistura de propriedades e métodos.
# print(canal_lyviaoc.nome, canal_lyviaoc.descricao, canal_lyviaoc.inscritos)
##
# canal_lancode = Canal("LanCode", "Códigos e gatos", 34000)
# # print(canal_lancode.nome, canal_lancode.descricao, canal_lancode.inscritos)
# #UTILIZANDO O METODO INSCREVER:
# print(f"Quantidade atual de inscritos: {canal_lancode.inscritos}")
# canal_lancode.inscrever(100)
# print(f"Quantidade atual de inscritos: {canal_lancode.inscritos}")
# ##

#Herança é quando uma classe criada herda tudo de outra classe ja existente.
#A classe CanalEmpresarial vai herdar da classe Canal

class Canal: #funcoes dentro de classes nao sao funcoes sao chamados metodos
    def __init__(self, nome, descricao, inscritos): #funcao __init__ chama-se metodo construtor #o parametro self passa a representar a instancia canal_lyviaoc e canal_lancode pois o metodo init foi chamado atraves do Canal
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists:list[Playlist] = []

    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print("Esse vídeo já foi postado!")
            return
        self.videos.append(video)

    def info_playlists(self):
        for playlist in self.playlists:
            print(playlist.nome)
            playlist.info_videos()

    def adicionar_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print("Essa playlist ja foi adicionada")

    def remover_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print("Essa playlist nao existe.")


class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos): #Apesar da classe herdar da outra e necessario colocar o init para iniciar direito
        super().__init__(nome, descricao, inscritos) #O super chama o metodo construtor init da classe Canal #O init novamente cria novas funcionalidades apenas para essa subclasse.
        self._equipe = []  # ENCAPSULAMENTO esconde/protege detalhes internos controlar como os dados são acessados usa métodos para interagir com esses dados #esta lista vazia representa a equipe que gerencia o canal
# o underline "_" antes de um atributo para indicar que este atributo nao deve ser modificado diretamente. "Esse atributo é interno da classe; não deveria ser acessado diretamente de fora."
    @property #com o @property nao e preciso colocar () toda vez que chamar o metodo equipe. #Ao modificar uma propriedade diretamente e perigoso, por isso e utilizado um tratamento para modificar ela em seguranca
    def equipe(self):
        return self._equipe
    def adicionar_membro_equipe(self, membro):
        if membro not in self.equipe:
            self._equipe.append(membro)
        else:
            print(f"O membro {membro} já encontra-se na equipe.")
    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f"O membro {membro}, nao esta na equipe.")

class Videos:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

        self.views = 0
        self.likes = 0
        self.deslikes = 0
        self.comments = []


    def __repr__(self):
        return f"<{self.titulo}>"

    def assistir(self):
        self.views += 1
        
    def curtir(self):
        self.likes += 1
    def descurtir(self):
        self.deslikes += 1

    def comentario(self, comments):
        self.comments.append(comments)

    def info_video(self):
        print(f"""Título: {self.titulo}
Descricao: {self.descricao}
{self.views} Visualizacoes
{self.likes} Likes  {self.deslikes} Deslikes
Comentários: {self.comments}""")

class Playlist(Canal):
    def __init__(self, nome):
        self.nome = nome
        self.videos:list[Videos] = []

    def adicionar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print("Este video ja esta na playlist.")

    def remover_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print("Este video nao esta na playlist.")

    def info_videos(self):
        for video in self.videos:
            video.info_video()


video_poo = Videos("Python objetos", "Aprenda agora!")
video_discordpy = Videos("Discord", "Automacoes")
video_minecraft = Videos("Minecraft", "Jogando minezin")

playlist_programacao = Playlist("Programacao")
playlist_programacao.adicionar_video(video_poo)
playlist_programacao.adicionar_video(video_discordpy)

playlist_mine = Playlist("Minecraft")
playlist_mine.adicionar_video(video_minecraft)

canal_lancode = Canal('Lan Code', 'Códigos e gatos', 34000)
canal_lancode.postar(video_poo)
canal_lancode.postar(video_discordpy)
canal_lancode.postar(video_minecraft)
canal_guanabara = Canal('Curso em Video', 'Paixão por ensinar', 10000)
canal_duolingo = CanalEmpresarial('Duolingo', 'ingres', 500000)

# print(canal_lancode.videos)
canal_lancode.adicionar_playlist(playlist_programacao)
canal_lancode.adicionar_playlist(playlist_mine)
canal_lancode.info_playlists()

# print(f"Membros atuais: {canal_duolingo.equipe}")
# canal_duolingo.adicionar_membro_equipe("Ana")
# print(f"Membros atuais: {canal_duolingo.equipe}")
# canal_duolingo.adicionar_membro_equipe("Pedro")
# canal_duolingo.remover_membro_equipe("Ana")
# canal_duolingo.adicionar_membro_equipe("Marcela")
# print(f"Membros atuais: {canal_duolingo.equipe}")
