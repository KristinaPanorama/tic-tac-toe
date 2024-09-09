from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.__size = 3
        self.pole = [[Cell() for _ in range(self.__size)] for _ in range(self.__size)]
        self.__is_human_win = False
        self.__is_human_win = False
        self.__is_draw = False

    def __check_index(self, i, j):
        if type(i) is not int or not (0 <= i < self.__size) or type(j) is not int or not (0 <= j < self.__size):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        i, j = item
        self.__check_index(i, j)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        self.__check_index(i, j)
        self.pole[i][j].value = value

    def show(self):
        for row in self.pole:
            for i in row:
                print('#' if i else 'x' if i.value == self.HUMAN_X else '0', end='')
            print()

    def init(self):
        for row in self.pole:
            for i in row:
                i.value = 0

    def human_go(self):
        i, j = map(int, input().split())
        if not (0 <= i <= self.__size) or not (0 <= j <= self.__size) and not self.pole[i][j]:
            raise ValueError()
        self.pole[i][j].value = self.HUMAN_X

    def computer_go(self):
        while game:
            i = randint(0, 2)
            j = randint(0, 2)
            if self.pole[i][j]:
                self.pole[i][j].value = self.COMPUTER_O
                break

    def __bool__(self):
        return not any([self.is_human_win, self.is_computer_win, self.is_draw])

    def get_list(self):
        return (*self.pole, *zip(*self.pole), [self.pole[0][0], self.pole[1][1], self.pole[2][2]],
                       [self.pole[0][2], self.pole[1][1], self.pole[2][0]])

    @property
    def is_human_win(self):
        self.__is_human_win = any(map(lambda x: all(map(lambda y: y.value == self.HUMAN_X, x)), self.get_list()))
        return self.__is_human_win

    @property
    def is_computer_win(self):
        self.__is_human_win = any(map(lambda x: all(map(lambda y: y.value == self.COMPUTER_O, x)), self.get_list()))
        return self.__is_human_win

    @property
    def is_draw(self):
        return not any(map(lambda x: any(map(lambda y: bool(y), x)), self.get_list()))


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")