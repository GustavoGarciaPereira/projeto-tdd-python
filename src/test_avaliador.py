from unittest import TestCase
from leilao.dominio import Leilao, Usuario, Lance, Avaliacao
import sys


class TastAvaliador(TestCase):
    def test_avaliador(self):
        gustavo = Usuario('gustavo')
        garcia = Usuario('garcia')

        lance_garcia = Lance(garcia, 5)
        lance_gustavo = Lance(gustavo, 12)

        leilao_cafe = Leilao('Café')

        leilao_cafe.lances.append(lance_garcia)
        leilao_cafe.lances.append(lance_gustavo)

        avaliacao = Avaliacao()

        avaliacao.avalia(leilao_cafe)

        self.assertEqual(5, avaliacao.menor)
        self.assertEqual(12, avaliacao.maior)
