import os
import sys
import shutil
import time
sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages")
from termcolor import colored



def game_restart():
    restart = input("Do you want to play again? Y/N: ")
    if restart == 'Y' or restart == 'y':
        os.system('clear')
        python = sys.executable
        os.execl(python, python, * sys.argv)

def player_rotation(currentPlayer, player1, player2):
    if currentPlayer == player1:
        currentPlayer = player2
    elif currentPlayer == player2:
        currentPlayer = player1
    return currentPlayer


def draw_board(board):
    lanes = colored("━━━╋━━━╋━━━", "yellow")
    col = colored("┃", "yellow")
    columns = shutil.get_terminal_size().columns

    print("    %s %s %s %s %s       ".center(columns) % (board[7], col, board[8], col, board[9]))
    print(lanes.center(columns))
    print("    %s %s %s %s %s       ".center(columns) % (board[4], col, board[5], col, board[6]))
    print(lanes.center(columns))
    print("    %s %s %s %s %s       ".center(columns) % (board[1], col, board[2], col, board[3]))

def waitBeforeClearingTerminal(sleepTime):
    time.sleep(sleepTime)
    os.system('clear')
    draw_board()

def sign_change(sign):
    if sign == 'X':
        return 'O'
    else:
        return 'X'

def wait4playerChoice(sign, currentPlayer):
    try:
        choice = int(input(colored("Pick your next move (" + currentPlayer + "'s turn)... ")))
        if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board[choice] == ' ':
            return choice
        else:
            print(colored("Nope!", "red"))
            waitBeforeClearingTerminal(1)
            return None
    except ValueError:
        print(colored("Play using numeric keyboard! ", "red"))
        waitBeforeClearingTerminal(1.3)
        return None

def check_win(board):
    for i in range (1, 8, 3):
        if board[i] == board[i+1] == board [i+2] and board[i] != ' ':
            return 'Win'
    for i in range (1, 4):
        if board[i] == board[i+3] == board [i+6] and board[i] != ' ':
            return 'Win'
    if board[3] == board[5] == board[7] and board[3] != ' ':
        return 'Win'
    if board[1] == board[5] == board[9] and board[1] != ' ':
        return 'Win'
    # Draw
    elif ' ' not in board:
        return "Draw"
    else:
        return "on"

def someone_wins(game, currentPlayer, board):
    if game == 'Win':
        os.system('clear')
        draw_board(board)
        print("%s wins!" % currentPlayer)

    elif game == 'Draw':
        os.system('clear')
        draw_board(board)
        print("It's a draw!")

# I want to play a game !


game = "on"
board = ['Too lazy to use 0 index', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
str(board)
sign = 'X'


os.system('clear')
player1 = str(input("Enter the name of the player 1: "))
if player1 == '':
    player1 = 'X'

player2 = str(input("Enter the name of the player 2: "))
if player2 == '':
    player2 = 'O'

if player1 == '':
    player1 = 'O'

if player2 == '':
    player2 = 'X'

if input(player1 + '! Type "O" if you want to start as O\'s instead of X\'s: ') == "O":
    sign = 'O'

currentPlayer = player1
os.system('clear')


while game == "on":
    os.system('clear')
    draw_board(board)
    currentSign = sign
    currentBoard = board
    choice = None
    while choice == None:
        choice = wait4playerChoice(sign, currentPlayer)
        if choice != None:
            board[choice] = sign
    sign = sign_change(sign)
    game = check_win(board)
    someone_wins(game, currentPlayer, board)
    currentPlayer = player_rotation(currentPlayer, player1, player2)

game_restart()

