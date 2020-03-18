# O jogo deverá sortear uma fruta conforme a lista abaixo:
# # - banana
# # - jabuticaba
# # - pitanga
# # - mirtilo
# # - morango
# # - abacaxi
# # - cereja
# #
# # O objetivo é acertar o nome da fruta. O jogador informa uma letra e o jogo verifica se a fruta tem essa letra.


import random

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo','morango', 'abacaxi', 'cereja']

self.fruta = random.choice(frutas)
class JogoFruta:
    def __init__(self):
        self.lista_frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo','morango', 'abacaxi', 'cereja']
        self.descobrir_palavra = ''
        self.vida = len(self.fruta)
        self.letras_corretas = []



#     def sorteia_fruta(self):
#         sorteio = randon.choice(self.lista_frutas)
#
# set
