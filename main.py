import os
import sys
import time
sys.path.append("/home/Patus/miniconda3/lib/python3.6/site-packages/console_menu-0.4.0-py3.6.egg")
#os.system("python3.6 ./PyTW_Week3/TicTacToeV2/TicTacToe.py")
from consolemenu import *
from consolemenu.items import *


os.system("clear")
os.system("toilet -f bigmono9 -F gay Tic Tac Toe")
time.sleep(2)
os.system("clear")

menu = ConsoleMenu("Tic Tac Toe", "Main menu")
command_item = CommandItem("Play!",  "cd /home/Patus/Desktop/Python/PyTW_Week3/TicTacToeV2; python3.6 TicTacToe.py")
menu.append_item(command_item)
menu.show()