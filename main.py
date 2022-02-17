from audioop import add
import random

#First define the variables that determine the board and the instruments of the game
#Global

board = []
rows = 10
cols = 8
ammo = 50
ship_position = [[]]
ships_sunk = 0
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index_board = []
position_shot = []



#Use dots to determine the grid position
def create_board(rows, cols):

    for x in range(rows):
        row = []
        for y in range(cols):
            row.append('.')         
        board.append(row)

    #Testing ships positions
    # for position in ship_position:
    #     for coord in position:
    #         board[coord[0]][coord[1]] = '#'


#Diferentiate the create from the print
def print_board():
    #board header left
    for row in range(len(board)):
        print(abc[row], end = ")  ")
        for col in range(len(board[row])):
            print(board[row][col], end = "  ")
        print("")

    #board header down  
    print("  ", end = "  ")
    for row in range(len(board[0])):
        print(str(row), end = "  ")
    print("")


def shipDirection(max, min, ship_length):
    direction = ["up", "left"]
    random_direction = random.choice(direction)
    random_position = [random.randint(0,max), random.randint(min,cols - 1)]
    shipPosition = []
    for ship in range(ship_length):
        if random_direction == "up":
            shipPosition.append((random_position[0] + ship, random_position[1]))
        elif random_direction == "left":
            shipPosition.append((random_position[0], random_position[1] - ship))
    return shipPosition

def randomly_ships_position(rows, cols):

    global ship_position

    ships = [4, 3, 3, 2, 2, 2]

    ship_position = []

    for ship in ships:
        ship_position.append(shipDirection(rows - ship - 1, ship - 1, ship))

def validations(rows, cols):
    global ammo

#validate if the coord was already passed or if it is out of range
    if index_board in position_shot or index_board[0] > (rows - 1) or index_board[1] > (cols - 1):
        ammo += 1
        print("Try a diferent move")
    


# determine board indexes
def  index_config(rows, cols):
#no puedo sacarla tampoco
    global index_board

    #create an array with the letters to locate its index
    input_coord =  input('write a coordinate:  ').upper()
    index_letter = []
    for letter in abc[0:rows]:
       index_letter.append(letter)
    
    #check the input and convert the letter coordinate to a number
    if input_coord[0] in index_letter:
        index_board = index_letter.index(input_coord[0]), int(input_coord[1])
    else:
        print('Write one possible coordinate')
    
    validations(rows, cols)
    
    position_shot.append(index_board)
 
def is_ship_sunk(ship):
    for ship_part in ship:
        if not ship_part in position_shot:
            return False
    return True

def shooting():
    global ships_sunk

    #testing
    #print(ship_position)

    #check if it reach an element of ship_position and change it to "0"
    for ship in ship_position:
        if index_board in ship:
            board[index_board[0]][index_board[1]] = 'O'
            print('\n'*5 + 'Shoot it !!'.upper() + '\n')
        
    # mark with a X the ship sunk
            if is_ship_sunk(ship):
                for ship_part in ship:
                    board[ship_part[0]][ship_part[1]] = "X"
                ships_sunk += 1
                print("Ship SUNK!!" + '\n'*2 + str(6 - ships_sunk) + " ships remained")
            break


#Game action
game = True
randomly_ships_position(rows,cols)
create_board(rows, cols)
print('\n' + 
"Instructions:" + '\n' + 
"1) ALWAYS WRITE A COORDINATE BEAFORE PRESSING ENTER" + '\n'
"2) CHOOSE A COORDINATE OF THE BOARD AND PRESS ENTER" '\n' +
"3) YOU WILL WIN WHEN ALL THE SHIPS ARE DOWN" + '\n' + 
"4) GOOD LUCK!" + '\n')
while ammo > 0 and ships_sunk < 6:
    ammo -= 1
    print_board()
    index_config(rows, cols)
    shooting()

    print(' Your ammo remaining is: ' + str(ammo))

print("FINISHED" + '\n'*5 + "YOU WON !!!!!" + '\n' * 5 + "CONGRATULATIONS !!!!" + '\n'*5)
    
