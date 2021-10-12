import random

# Пустая доска

head = list('  1 2 3')
line_1 = list('1\t\t\t')
line_2 = list('2\t\t\t')
line_3 = list('3\t\t\t')

default_board = [head, line_1, line_2, line_3]


class Board:

    """ Доска для игры """

    board = [head[:], line_1[:], line_2[:], line_3[:]]
    check_list = []

    def check_list_maker(self):

        """ Задает последовательность проверки клеток доски """

        self.check_list = []

        self.check_list.extend([self.board[i][1:] for i in range(1, 4)])
        self.check_list.extend([[self.board[i][j] for i in range(1, 4)] for j in range(1, 4)])

        self.check_list.append([self.board[i][i] for i in range(1, 4)])
        self.check_list.append([self.board[i][4 - i] for i in range(1, 4)])

    def reveal(self):

        """ Показывает доску """

        print()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()

    def clear(self):

        """ Очищает доску """

        self.board = [head[:], line_1[:], line_2[:], line_3[:]]
        self.check_list = []


class Human:

    """ Игрок """

    def __init__(self, name: str, mark: str):

        """ Передаем имя игрока и знак, которым он будет играть """

        self.name = name
        self.mark = '\t' + mark

    def make_a_move(self, brd: Board):

        """ Ход игрока """

        print('\nУкажите клетку. Через пробел указывается сначала горизонтальная,'
              'а затем вертикальная координата:', end=" ")
        point = input().split()

        if len(point) != 2 or (not point[0] in brd.board[0]) or (not point[1] in brd.board[0]):
            print('Что-то пошло не так. Попробуйте еще.')
            self.make_a_move(brd)
        elif brd.board[int(point[1])][int(point[0])] != '\t':
            print('Клетка уже занята. Попробуйте еще.')
            self.make_a_move(brd)
        else:
            brd.board[int(point[1])][int(point[0])] = self.mark


class Machine:

    """ Компьютер """

    name = "Computer"

    def __init__(self, mark: str):

        """ Передаем знак, которым будет играть компьютер """

        self.mark = '\t' + mark

    def search_target(self, brd: Board, i: int, j: list):

        """ Процесс выбора клетки для хода. Выбираем элемент из чек-листа """

        if i <= 3:
            brd.board[i][j.index('\t') + 1] = self.mark
        elif i <= 6:
            brd.board[j.index('\t') + 1][i - 3] = self.mark
        elif i == 7:
            brd.board[j.index('\t') + 1][j.index('\t') + 1] = self.mark
        elif i == 8:
            brd.board[j.index('\t') + 1][3 - j.index('\t')] = self.mark

    def attack(self, brd: Board):

        """ Агрессивное действие: формируем чек-лист и, если нет угрозы поражения при следующем ходе, атакуем """

        brd.check_list_maker()
        for i, j in enumerate(brd.check_list, 1):
            if j.count(self.mark) == 2 and j.count('\t') == 1:
                self.search_target(brd, i, j)
                break
        else:
            self.defence(brd)

    def defence(self, brd: Board):

        """ Защитное действие: формируем чек-лист и, если есть угроза поражения при следующем ходе, защищаемся """

        brd.check_list_maker()
        for i, j in enumerate(brd.check_list, 1):
            if len(set(j)) == 2 and j.count('\t') == 1:
                self.search_target(brd, i, j)
                break
        else:
            self.basic(brd)

    def basic(self, brd: Board):

        """
        Базовое действие: если не занята центральная клетка, занимаем ее.
        В противном случае занимаем любую свободную
        """

        i = 2
        j = 2
        while brd.board[i][j] != '\t':
            i = random.randint(1, 3)
            j = random.randint(1, 3)
        brd.board[i][j] = self.mark

    def make_a_move(self, brd: Board):

        """ Ход компьютера. Начинаем с попытки атаковать """

        self.attack(brd)

