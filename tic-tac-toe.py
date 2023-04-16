maps = [1, 2, 3,  # Создание карты
        4, 5, 6,
        7, 8, 9]

victories = [[0, 1, 2], [3, 4, 5],  # Варианты победных линий
             [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]


def print_maps():  # Вывод карты на экран
    print(maps[0], end=' ')
    print(maps[1], end=' ')
    print(maps[2])

    print(maps[3], end=' ')
    print(maps[4], end=' ')
    print(maps[5])

    print(maps[6], end=' ')
    print(maps[7], end=' ')
    print(maps[8])


def step_maps(step, symbol):  # Сделать ход в ячейку
    if step not in maps:
        try:
            try2 = int(input('Клетка занята, выберите другую: '))
            ind = maps.index(try2)
            maps[ind] = symbol
        except ValueError:
            step_maps(try2, symbol)
    else:
        ind = maps.index(step)
        maps[ind] = symbol


def get_result():  # Увидеть текущий результат игры
    win = ''

    for i in victories:
        if maps[i[0]] == 'x' and maps[i[1]] == 'x' and maps[i[2]] == 'x':
            win = 'x'
        elif maps[i[0]] == 'o' and maps[i[1]] == 'o' and maps[i[2]] == 'o':
            win = 'o'
        elif all([type(x) is str for x in maps]):
            win = 'ничья'

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:
    print_maps()

    if player1 == True:
        symbol = 'x'
        try:
            step = int(input('Игрок 1, ваш ход: '))
        except ValueError:
            print('Введите число!')
            step = int(input('Игрок 1, ваш ход: '))
    else:
        symbol = 'o'
        try:
            step = int(input('Игрок 2, ваш ход: '))
        except ValueError:
            print('Введите число!')
            step = int(input('Игрок 2, ваш ход: '))

    step_maps(step, symbol)
    win = get_result()
    if win != '':
        game_over = True
    else:
        game_over = False

    player1 = not player1

print_maps()  # Когда игра окончена покажем карту и объявим победителя
print(f'Победил(а) {win}!')