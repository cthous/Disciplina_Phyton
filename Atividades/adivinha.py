import random

numero_aleatorio = random.randint(1, 300)

while True:
    numero_escolhido = int(input('Escolha um número entre 1 e 300: '))
    if numero_escolhido < 1 or numero_escolhido > 300:
        print('Eu disse um número ENTRE 1 e 300.')
    elif numero_escolhido < numero_aleatorio:
        print('Quase. Tente um número maior')
    elif numero_escolhido > numero_aleatorio:
        print('Quase. Tente um número menor')
    else:
        print('Parabéns! Você acertou o número.')
        break