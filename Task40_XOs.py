# Задача 40.
# Вы когда-нибудь играли в игру "Крестики-нолики"?
# Попробуйте создать её.

ground = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def print_ground(ground):
    for element in ground:
        print(element)

def player_1_move(ground, player1):
    for element in ground:
        for i in range(len(element)):
            if element[i] == player1:
                element[i] = 'X'

def player_2_move(ground, player1):
    for element in ground:
        for i in range(len(element)):
            if element[i] == player1:
                element[i] = 'O'

print_ground(ground)

count = 0
while count < 10:
    player1 = int(input('Игрок 1 вводит цифру: '))
    player_1_move(ground, player1)
    print_ground(ground)
    count +=1
    if count == 9:
        print("КОНЕЦ ИГРЫ")
        break
    player1 = int(input('Игрок 2 вводит цифру: '))
    player_2_move(ground, player1)
    print_ground(ground)
    count +=1