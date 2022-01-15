import curses
from tabulate import tabulate

#configure the window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Classes
grid = []
col = int(input())
row = int(input())



#game logic

while True:
   event = win.getch()

   #assign data
   data = []

   #headers
   head = ["Name", "City"]

   #display table
   print(tabulate(data, headers=head, tablefmt="grid"))




curses.endwin()
print("You win!")
