
from initial_setting import *


def win_check(brd: Board, plr: (Human, Machine)):

    """ Проверка на выигрыш """

    brd.check_list_maker()
    for line in brd.check_list:
        if line.count(plr.mark) == 3:
            print('Выиграл {}'.format(plr.name))
            return True
    return False


def tie_check(brd: Board):

    """ Проверка на ничью """

    brd.check_list_maker()
    for line in brd.check_list:
        if line.count('\t') != 0:
            return False
    print('Ничья')
    return True


board_1 = Board()
player_1 = Human('Player', 'x')
player_2 = Machine('0')

board_1.clear()
board_1.reveal()

while True:
    for player in player_1, player_2:
        player.make_a_move(board_1)
        board_1.reveal()
        if win_check(board_1, player) or tie_check(board_1):
            board_1.clear()
            board_1.reveal()
            break

