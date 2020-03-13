
import random

#cartas  = [ '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
valores  = [{'carta 2': 2}, {'carta 3': 3}, {'carta 4': 4}, {'carta 5': 5},{'carta 6': 6}, {'carta 7': 7}, {'carta 8': 9},
            {'carta 9': 9}, {'carta 10': 10}, {'carta J': 10}, {'carta Q': 10}, {'carta K': 10}, {'carta A': 11}]
quantidade = 1
valor = 0
contador = 0

while (quantidade > 0):
    virar_carta = int(input('Deseja virar carta? (1-Yes / 0-No):'))
    if virar_carta == 1:
        escolha = random.choice(valores)
        print(escolha)
        continue
    if virar_carta == 0:
        break

    for i in valores:
        if i ==  :
            if i == 'A':
                if valor == 0:
                    valor = valor + 11
                else:
                    valor = valor + 1
            else:
                valor = valor + valores[i]
            print(f"Valor: {valor}")
    contador += 1


#
#         # else:
#     #         #     quantia = quantidade - 1
#     #         #     print(f'Score:{valor}')
#
# def pegar_carta(baralho):
#     escolhido = random.choice(baralho)
#     indice = baralho.index(escolhido)
#     baralho[indice]
#     return escolhido