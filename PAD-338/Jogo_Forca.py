
import random

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo','morango', 'abacaxi', 'cereja']

class JogoFruta:
    def __init__(self):
        self.frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo','morango', 'abacaxi', 'cereja']
        self.tentativas_letras = ''
        self.palavra_descoberta = ''

    def jogar (self):
        self.sorteio = random.choice(self.frutas)
        while True:
            self.tentativas_letras = input('Digite uma letra da palavra a ser descoberta:')


    def sorteio_fruta(self):
         self.sorteio = random.choice(self.frutas)


        





jf = JogoFruta()
jf.jogar()