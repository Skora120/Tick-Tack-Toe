import os

#TODO
#fix input
#input validation

init = False
fields = {'4': ' ', '9': ' ', '2': ' ', '3': ' ', '5': ' ', '7': ' ', '8': ' ', '1': ' ', '6': ' '}
player1 = None
player2 = None


def clear_screen():
    os.system('cls')


def check_for_win():
    score_row = 0
    score_first_col = 0
    score_second_col = 0
    score_third_col = 0
    score_first_diagonal = 0
    score_second_diagonal = 0
    current_item = 1

    for value in fields.items():
        # row win check
        if value[1] == player1:
            score_row += int(value[0])

        elif value[1] == player2:
            score_row -= int(value[0])

        if 15 in (score_row, score_first_col, score_second_col, score_third_col, score_first_diagonal, score_second_diagonal):
            print("Player1 has won!")
            return 1
        elif -15 in (score_row, score_first_col, score_second_col, score_third_col, score_first_diagonal, score_second_diagonal):
            print("Player2 has won!")
            return 1

        # for diagonal check
        if int(value[0]) == 8 or int(value[0]) == 2:
            if value[1] == player1:
                score_first_diagonal += int(value[0])
            elif value[1] == player2:
                score_first_diagonal -= int(value[0])

        elif int(value[0]) == 6 or int(value[0]) == 4:
            if value[1] == player1:
                score_second_diagonal += int(value[0])
            elif value[1] == player2:
                score_second_diagonal -= int(value[0])

        if int(value[0]) == 5:
            if value[1] == player1:
                score_first_diagonal += int(value[0])
                score_second_diagonal += int(value[0])

            elif value[1] == player2:
                score_first_diagonal -= int(value[0])
                score_second_diagonal -= int(value[0])

        print(score_first_diagonal, score_second_diagonal)

        if current_item % 3 == 0:
            # for row check
            score_row = 0
            # for col 1 check
            if value[1] == player1:
                score_first_col += int(value[0])

            elif value[1] == player2:
                score_first_col -= int(value[0])
        elif current_item % 3 == 1:
            if value[1] == player1:
                score_second_col += int(value[0])

            elif value[1] == player2:
                score_second_col -= int(value[0])
        else:
            if value[1] == player1:
                score_third_col += int(value[0])

            elif value[1] == player2:
                score_third_col -= int(value[0])

        current_item += 1

    return 0


def restart():
    global fields
    fields = {'4': ' ', '9': ' ', '2': ' ', '3': ' ', '5': ' ', '7': ' ', '8': ' ', '1': ' ', '6': ' '}
    draw_board()
    update()


def mark(arg):
    global fields
    field = int(input("{}: choose field: ".format(arg)))
    fields[list(fields.keys())[abs(field-1)]] = arg


def update():
    global player1, player2
    # check for win / draw move
    number_of_moves = 0
    player1_turn = True
    print("test")
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

    if input("Do you wish to play again? Type 'Y'").lower() == "y":
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

    print("Fields on board respond to numpad keys")
    input("Press any key to start!")

    draw_board()
    init = True
    update()


setup()