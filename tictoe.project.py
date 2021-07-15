                 # Project # 1 -----> Tic-toe Game
import random

game_input = ['Null', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

def board(game_input) :
    print(game_input[7]+ '|'+ game_input[8]+ '|'+ game_input[9])
    print(game_input[4]+ '|'+ game_input[5]+ '|'+ game_input[6])
    print(game_input[1]+ '|'+ game_input[2]+ '|'+ game_input[3])

# board(game_input)

def player_input():

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Enter your choice')
    if marker == 'X':                                   # and marker == 'O'
        return ('X', 'O')
    else:
        return ('O', 'X')
# player_input()

# player1, player2 = player_input()
# print(player1)
# print(player2)

def put_marker(game_input,marker,position):
    game_input[position] = marker



def win(game_input,marker):
    return  ((game_input[1] == game_input[2] == game_input[3] == marker )or
    (game_input[4] == game_input[5] == game_input[6] == marker ) or
    (game_input[7] == game_input[8] == game_input[9] == marker ) or

    (game_input[1] == game_input[4] == game_input[7] == marker)  or
    (game_input[2] == game_input[5] == game_input[6] == marker ) or
    (game_input[3] == game_input[6] == game_input[9] == marker ) or

    (game_input[1] == game_input[5] == game_input[9] == marker ) or
    (game_input[7] == game_input[5] == game_input[3] == marker ))

# print(win(game_input, 'O'))


# Choose player randomly using random function

def choose_player():
    player = random.randint(1, 2)

    if player == 1:
        return 'player_1'
    else:
        return 'player_2'

# Check for empty space

def space(game_input, position):
    return game_input[position] == ' '


# Full board check
def full_board_check(game_input):
    for i in range(1, 10):
        if space(game_input, i):
            return False
    return True

# Player Choice if marker placement

def player_choice_position(game_input):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not  space(game_input, position):
        position = int(input('Please choose your position(1-9) on NumPad'))
    return position

# Play again

def play_again():
    choice = 'Would you like to play again [Y/N]'
    return choice == 'Y'

# GAme playing mechanism

while True:
    the_board = [' '] * 10
    player_1, player_2 = player_input()
    print(player_1 + ' will play first')
    print(player_2 + ' will play first')

    turn = choose_player()
    print(turn + ' will play first')

    play_game = input('Are you Ready To Play A Game [Y/N]:')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player_1':
            board(the_board)
            position = player_choice_position(the_board)
            put_marker(the_board, player_1, position)

            if win(the_board, player_1):
                board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('The Tie')
                    game_on = False
                else:
                    turn = player_2

        else:
            board(the_board)
            position = player_choice_position(the_board)

            put_marker(the_board, player_2, position)

            if win(the_board, player_2):
                board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    board(the_board)
                    print('The Tie')
                    game_on = False

                else:
                    turn = 'player_1'
    if not play_again():
        break 