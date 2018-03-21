import os
import sys
import shutil
import time
sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages")
from termcolor import colored


game = "on"
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
str(board)
sign = 'X'


def player_rotation():
    global currentPlayer
    global player1
    global player2

    if currentPlayer == player1:
        currentPlayer = player2
    elif currentPlayer == player2:
        currentPlayer = player1


def draw_board():
    lanes = colored("━━━╋━━━╋━━━", "yellow")
    col = colored("┃", "yellow")
    columns = shutil.get_terminal_size().columns

    print("    %s %s %s %s %s       ".center(columns) % (board[7], col, board[8], col, board[9]))
    print(lanes.center(columns))
    print("    %s %s %s %s %s       ".center(columns) % (board[4], col, board[5], col, board[6]))
    print(lanes.center(columns))
    print("    %s %s %s %s %s       ".center(columns) % (board[1], col, board[2], col, board[3]))

def waitBeforeClearingTerminal(n):
    time.sleep(n)
    os.system('clear')
    draw_board()

def wait4player(board, sign, game):
    try:
        choice = int(input(colored("Pick your next move (" + currentPlayer + "'s turn)... ")))
        if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board[choice] == ' ':
            board[choice] = sign
            if sign == 'X':
                sign = 'O'
            elif sign == 'O':
                sign = 'X'
            check_win(board, sign, game)
        else:
            print(colored("Nope!", "red"))
            waitBeforeClearingTerminal(1.5)
    except ValueError:
        print("Play using numeric keyboard! ")


def check_win(board, sign, game):
    # Horizontal
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        game = "Win"

    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        game = "Win"

    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        game = "Win"

    # Vertical
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        game = "Win"

    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        game = "Win"

    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        game = "Win"

    # Diagonal
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        game = "Win"

    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        game = "Win"

    # Draw
    elif ' ' not in board:
        game = "Draw"

    if game == 'Win':
        os.system('clear')
        draw_board()
        print("%s wins!" % currentPlayer)
    if game == 'Draw':
        os.system('clear')
        draw_board()
        print("Draw!")

# I want to play a game !


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
    draw_board()
    currentSign = sign
    while currentSign == sign:
        wait4player(board, sign, game)
    player_rotation()

restart = input("Do you want to play again? Y/N: ")
if restart == 'Y' or restart == 'y':
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)
