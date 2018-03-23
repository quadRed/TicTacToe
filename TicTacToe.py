import os
import sys
import shutil
import time
sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages")
from termcolor import colored
# sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages/console_menu-0.4.0-py3.6.egg")
# from consolemenu import *
# from consolemenu.items import *


def initializePlayer(number):
    player = str(input("Enter the name of the player %s: " % number))
    if player == '':
        print("Ok, your name will be your sign!")
        time.sleep(1.2)
        os.system('clear')
        return ''
    else:
        print("Hello, %s!" % player)
        time.sleep(1)
        os.system('clear')
        return player

def players_choose_sign():
    signsList = []
    signHasBeenChosen = False
    while not signHasBeenChosen:
        chosenSign = input("Player 1! Choose either \"X\" or \"O\": ")
        if chosenSign == 'X' or chosenSign == 'O':
            signsList += [chosenSign]
            if chosenSign == 'X':
                signsList += ['O']
            else:
                signsList += ['X']

            signHasBeenChosen = True
        else:
            print(colored("I said X or O, honey", "red"))
            time.sleep(1)
            os.system("clear")
    return signsList

def game_restart():
    restart = input("Need a quick restart? (Y/y). \nAnything else will send you to the main menu.\n")
    if restart == 'Y' or restart == 'y':
        os.system('clear')
        python = sys.executable
        os.execl(python, python, * sys.argv)
    else:
        os.system('clear; exit')

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
    draw_board(board)

def sign_change(sign, signTable):
    if sign == signTable[0]:
        return signTable[1]
    else:
        return signTable[0]

def wait4playerChoice(sign, currentPlayer):
    try:
        if currentPlayer == sign:
            choice = int(input(colored("Pick your next move (" + currentPlayer + "'s turn)... ")))
        else:
            choice = int(input(colored("Pick your next move (" + currentPlayer + "'s turn - %s)... " % sign)))
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
        os.system("figlet Congrats")

    elif game == 'Draw':
        os.system('clear')
        draw_board(board)
        print("It's a draw!")

# I want to play a game !

game = "on"
board = ['Too lazy to use 0 index', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
str(board)
os.system('clear')
signTable = []

player1 = initializePlayer('1')
player2 = initializePlayer('2')

signTable = players_choose_sign()
sign = signTable[0]

if player1 == '':
    player1 = signTable[0]
if player2 == '':
    player2 = signTable[1]

currentPlayer = player1
os.system('clear')

#Main game loop

while game == "on":
    os.system('clear')
    draw_board(board)
    choice = None
    while choice == None:
        choice = wait4playerChoice(sign, currentPlayer)
        if choice != None:
            board[choice] = sign
    sign = sign_change(sign, signTable)
    game = check_win(board)
    someone_wins(game, currentPlayer, board)
    currentPlayer = player_rotation(currentPlayer, player1, player2)

time.sleep(2)
os.system('clear')
game_restart()

