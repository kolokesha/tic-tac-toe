import random


def print_board(history):
    print(f"{history[7]}|{history[8]}|{history[9]}\n- - -\n{history[4]}"
          f"|{history[5]}|{history[6]}\n- - -\n{history[1]}|{history[2]}|{history[3]}")

def choose_char():
    print('За кого играем? Х или О')
    player2 = ''
    player1 = input()
    if player1 == 'x' or player1 == 'X':
        player2 = 'o'
    elif player1 == 'o' or player1 == 'O':
        player2 = 'x'
    else:
        print('Неправильный ввод, введите еще раз!')
        choose_char()
    return (player1, player2)

def winning_check(history):
    return True

def is_space(history, i):
    if history[i] == ' ':
        return True
    else:
        return False

def insert_marker(history, i, char):
    history[i] = char
    print_board(history)

def main_game(history, player1_char):
    if player1_char == 'x':
        print('Первыми ходят крестики')
        player2_char = 'o'
    else:
        print('Первыми ходят нолики')
        player2_char = 'x'
    count = 0
    while winning_check(history) == True:
            print('Введите число 1-9 чтобы поставить свой знак')
            i = int(input())
            if count == 0:
                insert_marker(history, i, player1_char)
                player1_char, player2_char = player2_char, player1_char
                count += 1
            else:
                if is_space(history, i) == True:
                    insert_marker(history, i, player1_char)
                    print(history)
                    player1_char, player2_char = player2_char, player1_char
                    count += 1
                else:
                    print('Там уже есть символ, введите новый')
            print(f'{count} zzz')

def who_is_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    history = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    player1_char, player2_char = choose_char()
    if who_is_first() == 0:
        main_game(history, player1_char)
    else:
        main_game(history, player2_char)