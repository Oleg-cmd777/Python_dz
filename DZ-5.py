# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


line = 'Гикбрейнс всех научит'
words = line.split(' ')
fragment = str(input("Введи фрагмент "))
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
print(' '.join(new_words))

# 2. Создайте программу для игры с конфетами человек против человека.
#
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
#
import random
from random import randint, choice

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']
max_number_move = 0


def introduce_players():
    player1 = 'player1'
    player2 = 'BOT'
    print(f'Вы играете с искуственным  {player2}')
    return [player1, player2]


def sweets_game(players):
    global max_number_move
    total_sweets = 150
    max_number_move = 28
    first = 0
    return [total_sweets, max_number_move, first]


max_move = max_number_move


def game_player_vs_smart_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]

    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Я забираю {move}')

        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


players = introduce_players()
sweets = sweets_game(players)

winer = game_player_vs_smart_bot(sweets, players, messages)
if not winer:
    print('Ничья')
else:
    print(
        f'Победил {winer}!')

#3. Создайте программу для игры в 'Крестики-нолики'.
# print("*" * 10, "Крестики-нолики", "*" * 10)
#
board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Неверный ввод.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input("Нажмите Enter для выхода!")


#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
#Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc
with open('file.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_1.txt', 'r') as data:
    string = data.readline()

def f_enc(dec_s):
    enc_s = ''
    count = 1
    char = dec_s[0]
    for i in range(1, len(dec_s)):
        if dec_s[i] == char:
            count += 1
        else:
            enc_s = enc_s + str(count) + char
            char = dec_s[i]
            count = 1
            enc_s = enc_s + str(count) + char
    return enc_s


def f_dec(enc_s):
    dec_s = ''
    char_amount = ''
    for i in range(len(enc_s)):
        if enc_s[i].isdigit():
            char_amount += enc_s[i]
        else:
            dec_s += enc_s[i] * int(char_amount)
        char_amount = ''
    print(dec_s)

    return dec_s


with open('file.txt', 'r') as file:
    dec_s = file.read()

with open('file_1.txt', 'w') as file:
    enc_s = f_enc(dec_s)
    file.write(enc_s)

print('Decoded string: \t' + dec_s)
print('Encoded string: \t' + f_enc(dec_s))
print(f'Compress ratio: \t{round(len(dec_s) / len(enc_s), 1)}')