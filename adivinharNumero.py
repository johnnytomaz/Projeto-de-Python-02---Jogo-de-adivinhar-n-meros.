import random

print('Seja bem-vindo ao nosso jogo de adivinhação numérica!')
choice_number = input('Digite o número limite para o desafio: ')

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Erro: o valor informado não é um número. Por favor, tente novamente..')
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input('Adivinhe o número:')

    if answer_user.isdigit():
        answer_user = int(answer_user)

    else:
        print('Erro: valor informado não é um número. Por favor, tente novamente.')
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print('Você acertou!')
        break
    elif answer_user > random_number:
        print('Chutou alto! Tente novamente.')
    else:
        print('Número baixo! Tente novamente.')

print(f'Número de tentativas: {n_choices}')