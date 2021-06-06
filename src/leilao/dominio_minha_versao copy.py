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
        self.maior = 0

    @property
    def lances(self):
        return self.__lances

    def fazer_lance(self, lance):
        '''
        qual é o maior e o menor lance do que foidado
        '''

        self.lances.append(lance)
        if lance.valor > self.maior:
            self.maior = lance.valor

        try:
            if self.menor > lance.valor:
                self.menor = lance.valor
        except Exception:
            self.menor = lance.valor
