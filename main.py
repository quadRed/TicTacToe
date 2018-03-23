import os
import sys
sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages/console_menu-0.4.0-py3.6.egg")
#os.system("python3.6 ./PyTW_Week3/TicTacToeV2/TicTacToe.py")
from consolemenu import *
from consolemenu.items import *


menu = ConsoleMenu("Tic Tac Toe", "Main menu")
command_item = CommandItem("Play!",  "python3.6 ./PyTW_Week3/TicTacToeV2/TicTacToe.py")
menu.append_item(command_item)
menu.show()