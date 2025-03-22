from random import *

new_game = 'да'
print('Добро пожаловать в числовую угадайку')


def is_valid(a):
    if a.isdigit() and 1 <= int(a) <= granica:
        return True
    return False


while new_game == 'да':
    print('Введите максимальное натуральное число которое мы можем загадать.')
    granica = int(input())
    WiFi = True
    y = randint(1, granica)
    attempts = 0
    while WiFi:
        num = input()
        if is_valid(num):
            num = int(num)
            attempts += 1
            if y < num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif y > num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print(f'Кол-во потраченных попыток: {attempts}')
                WiFi = False
        else:
            print(f'А может быть все-таки введем целое число от 1 до {granica}?')
    print('Если хотите сыграть еще раз напишите "да"')
    new_game = input()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')