class Usuario:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome_q(self):
        return self.__nome


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

    @property
    def nome_valor(self):
        return f"nome: {self.usuario.nome} | valor: {self.valor}"


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []  # atributo privador '__'

    @property
    def lances(self):
        return self.__lances
