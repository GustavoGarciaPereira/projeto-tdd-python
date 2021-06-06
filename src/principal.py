from leilao.dominio import Leilao, Usuario, Lance, Avaliacao

gustavo = Usuario('gustavo')
garcia = Usuario('garcia')


lance_gustavo = Lance(gustavo, 12)
lance_garcia = Lance(garcia, 5)

leilao_cafe = Leilao('Café')

leilao_cafe.lances.append(lance_gustavo)
leilao_cafe.lances.append(lance_garcia)


for i in leilao_cafe.lances:
    print(i.nome_valor)


avaliacao = Avaliacao()
avaliacao.avalia(leilao_cafe)

print(f"avaliacao.maior: {avaliacao.maior}")
print(f"avaliacao.meior: {avaliacao.meior}")
