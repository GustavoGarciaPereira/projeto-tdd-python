import sys
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


class Avaliacao:
    def __init__(self):
        self.maior = sys.float_info.min
        self.menor = sys.float_info.max

    def avalia(self, leilao: Leilao):
        for i in leilao.lances:
            if i.valor > self.maior:
                self.maior = i.valor

            if i.valor < self.menor:
                self.menor = i.valor
