
# As cartas utilizadas e valores serão conforme abaixo:
# "2" => 2
# "3" => 3
# "4" => 4
# "5" => 5
# "6" => 6
# "7" => 7
# "8" => 8
# "9" => 9
# "10" => 10
# "A" => 1
# "J" => 10
# "Q" => 10
# "K" => 10
#
# O jogo deverá embaralhar as cartas acima. O jogo deve pedir para o jogador virar uma cartão,
# quando ele virar, deverá apresentar o score de acordo com a carta.
#
# Obs.: O "A" terá o valor 1 quando tiver outro número já virado.
#
# Segue exemplo abaixo:
# ["A"] ==> 11
# ["A", "J"] ==> 21
# ["A", "10", "A"] ==> 12
# ["5", "3", "7"] ==> 15
# ["5", "4", "3", "2", "A", "K"] ==> 25
# jogador
#croupier
#valete, dama e reis = 10 pontos
# ás 1 ou 10 pontos de acordo com a vontade do jogador

import random

class BlackJack:
    def __init__(self):
        self.lista_cartas = ['A','1', '2', '3', '4', '5','6', '7', '8','9', '10',{'K':10, 'J':10, 'Q':10}]
        self.play = True

    def embaralhar_cartas(self, lista_cartas):
        pass

    def mesa(self):
        pass