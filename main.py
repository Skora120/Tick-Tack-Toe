import os

init = False
fields = {'4': ' ', '9': ' ', '2': ' ', '3': ' ', '5': ' ', '7': ' ', '8': ' ', '1': ' ', '6': ' '}
player1 = None
player2 = None


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_for_win():
    score = {'row': 0, 'col_first': 0, 'col_second': 0, 'col_third': 0, 'diagonal_first': 0, 'diagonal_second': 0}
    current_item = 1

    for value in fields.items():
        # row win check
        if value[1] == player1:
            score['row'] += int(value[0])

        elif value[1] == player2:
            score['row'] -= int(value[0])

        # for diagonal check
        if int(value[0]) == 8 or int(value[0]) == 2:
            if value[1] == player1:
                score['diagonal_first'] += int(value[0])
            elif value[1] == player2:
                score['diagonal_first'] -= int(value[0])

        elif int(value[0]) == 6 or int(value[0]) == 4:
            if value[1] == player1:
                score['diagonal_second'] += int(value[0])
            elif value[1] == player2:
                score['diagonal_second'] -= int(value[0])

        if int(value[0]) == 5:
            if value[1] == player1:
                score['diagonal_first'] += int(value[0])
                score['diagonal_second'] += int(value[0])

            elif value[1] == player2:
                score['diagonal_first'] -= int(value[0])
                score['diagonal_second'] -= int(value[0])

        # print(score)

        for scr in score.values():
            if scr == 15:
                print("Player1 has won!")
                return 1
            elif scr == -15:
                print("Player2 has won!")
                return 1

        if current_item % 3 == 0:
            # for row check
            score['row'] = 0
            # for col 1 check
            if value[1] == player1:
                score['col_first'] += int(value[0])

            elif value[1] == player2:
                score['col_first'] -= int(value[0])
        elif current_item % 3 == 1:
            if value[1] == player1:
                score['col_second'] += int(value[0])

            elif value[1] == player2:
                score['col_second'] -= int(value[0])
        else:
            if value[1] == player1:
                score['col_third'] += int(value[0])

            elif value[1] == player2:
                score['col_third'] -= int(value[0])

        current_item += 1

    return 0


def restart():
    global fields
    fields = {'4': ' ', '9': ' ', '2': ' ', '3': ' ', '5': ' ', '7': ' ', '8': ' ', '1': ' ', '6': ' '}
    clear_screen()
    draw_board()
    update()


def mark(arg):
    global fields
    while True:
        field = input("{}: choose field: ".format(arg))

        if ord(field[0]) in range(49, 58) and fields[list(fields.keys())[abs(int(field[0]) - 1)]] == ' ':
            fields[list(fields.keys())[abs(int(field[0]) - 1)]] = arg
            break


def update():
    global player1, player2
    # check for win / draw move
    number_of_moves = 0
    player1_turn = True
    while not check_for_win():
        if number_of_moves >= 9:
            print("Draw")
            break
        elif player1_turn:
            mark(player1)
            player1_turn = False
        else:
            mark(player2)
            player1_turn = True

        clear_screen()
        draw_board()
        number_of_moves += 1

    if input("Do you wish to play again? Type 'Y': ").lower() == "y":
        restart()


def draw_board():
    global fields
    if init:
        print("  {}  |  {}  |  {}  ".format(fields['8'], fields['1'], fields['6']))
        print("------------------")
        print("  {}  |  {}  |  {}  ".format(fields['3'], fields['5'], fields['7']))
        print("------------------")
        print("  {}  |  {}  |  {}  ".format(fields['4'], fields['9'], fields['2']))
    else:
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")


def setup():
    global player1, player2, init

    player1 = input("Type 1 for be X or 2 for O: ")

    if player1 != "2":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    print("You have choose: {}".format(player1))

    print("Fields on board respond to NumPad keys")
    input("Press any key to start!")

    draw_board()
    init = True
    update()


setup()
