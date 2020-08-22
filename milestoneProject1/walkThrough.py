# tic tac toe game correction
import random
import os

# Global variables

board = [' '] * 10
display_board(board)
game_state = True
announcement = ''

def clear():
    os.system('cls')

def reset_board():
    global board, game_state
# Board setup
def display_board(board):

    # clear output
    clear()

    # print the playing board, the game will ignore the 0 index
    print('   |   |')
    print(' ' + board[7] +  ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-------------')
    print('   |   |')
    print(' ' + board[4] +  ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(' ' + board[1] +  ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')



# write a function that can take in a playeer input and
# assign their marker 'X' or 'O'

def player_input():
    marker = ''

    while not (marker == 'O' or marker == 'X'): # while marker is not equal to x or o keep asking for input 
        marker = input('Player 1: Do you want to be X or O').upper()

        if marker == X:
            return ('X', 'O')
        else:
            return ('O', 'X')


# wtitea function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the boards

def place_marker(board, marker, position):
    board[position] = marker

# Write a func that takes in a board and a mark (X or O) and then checks 
# to see if the mark has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # acroos the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # dwon the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # dwon the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# write a functino that used the random module to randomly decide which player goes first 
def choose_first_player():
    if random.randint(0,1) == 0: # if this returns a number between 0 and 1 and the returned int is 0 then do the following
        return 'Player1'
    else:
        return 'Player2'

# Wrtie a function that returns a boolean indicating whether a space in the board is freely available
def space_check(board, position):
    return board[position] == ' ' # if the position on the board is equal to a space return true else false

# Wrtie a function to check if the board is full and retruns a boolean value. Tru if full, False if otherwise
def full_board_check(board):
    for i in range(1, 10): # the board is number from 1 - 9, so this checks from range 1 to 9 excluding 10 itself and uses the index i to check every position on the board
        if space_check(board, i): 
            return False # bcos if the function is true or returns true that means there is a free or empty space which also means there is a the board isnt full
    
    return True

# Write a function that asks for a player's next position(as a number 1-9) and then uses
# the function from step 6 to check if its a free position. If it is, then return the position for later use
def player_choice(board):
    position = ' '

    # while the position from the input picked by the player is not in the list created or not in taken using the space_check function to check 
    # then keep prompting to enter position as input
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')

# Write a function to ask a player
def replay():
    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')


# my_string = 'Yup'
# my_string.lower().startswith('y') should return true or false

