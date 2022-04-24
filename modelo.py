class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
