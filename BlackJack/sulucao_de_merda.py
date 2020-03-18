import random

class BlackJack:
    def __init__(self):
        self.valores_cartas =[{'carta 2': 2}, {'carta 3': 3}, {'carta 4': 4}, {'carta 5': 5}, {'carta 6': 6}, {'carta 7': 7}, {'carta 8': 9},
        {'carta 9': 9}, {'carta 10': 10}, {'carta J': 10}, {'carta Q': 10}, {'carta K': 10}, {'carta A': 11}]
        self.quantidade_jogadores = 0
        self.nome_jogador = []
        self.jogador_vez = 0
        self.croupier = None

    def numero_jogadores(self):
        self.quantidade_jogadores = int (input('Digite a quantidade de jogadores:'))
        print(f'A quantidade de jogadores é {self.quantidade_jogadores}')
        self.obter_jogadores()

    def obter_jogadores(self):
        quantidade = 0
        while (quantidade < self.quantidade_jogadores):
            self.nome_jogador.append({
                'nome': input('Digite o nome do jogador'),
                'total pontos': 0})
            quantidade +=1
            print(quantidade)

    def embaralhar(self):
       for i in range(len(self.nome_jogador)):
           virar_carta = input('deseja virar carta? (1-Yes / 0-No):')

           while (virar_carta == '1'):
               escolha = random.choice(self.valores_cartas)
               self.nome_jogador[i]['total pontos'] = self.nome_jogador[i]['total pontos'] + escolha["valor"]
               print(self.nome_jogador[i]['total pontos'])
               virar_carta = input('Jogador ' + self.nome_jogador[i]['nome'] + ' deseja virar carta? (1-Yes / 0-No):')



    # def verifica_pontos(self):
    #     pass
    #

bk = BlackJack()
bk.numero_jogadores()
bk.embaralhar()

