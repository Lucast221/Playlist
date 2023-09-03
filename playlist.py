class Programa:  # Classe mãe
    def __init__(self, nome, ano):
        print("Construindo um objeto filme {}".format(self))
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        print("Você acabou de curtir este filme!")
        self._likes += 1


class Filme(Programa):  # Classe filha
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def descricao(self):
        print(
            f"Filme: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}")

# ------------------------------------------------------------------------------------------------------------------------------


class Serie(Programa):  # Classe filha
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def descricao(self):
        print(
            f"Série: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporada} - Likes: {self.likes}")
