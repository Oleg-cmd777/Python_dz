# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])

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

    # 3. Создайте программу для игры в 'Крестики-нолики'.
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

    dp.register_message_handler(commands.finish, commands=['finish'])
    # dp.register_message_handler(commands.set_count, commands=['set_count'])
    #
    dp.register_message_handler(commands.getNumber)