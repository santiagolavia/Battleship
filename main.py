import random

#First define the variables that determine the board and the instruments of the game
#Global
board = [[]]
rows = 10
cols = 8
ammo = 50
ships = 6
ship_position = [[]]
ships_sunk = 0
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#Use dots to determine the grid position
def create_board(rows, cols):

    global board
    global abc

    board = []
    #board
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append('.')         
        board.append(row)

    for i in ship_position:
        for x in i:
            board[x[0]][x[1]] = '#'

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



#print(board)

def randomly_ships_position(rows, cols):

    global board
    global ships
    global ship_position

    ships_placed = 0
    ship_2 = 3
    ship_3 = 2
    ship_4 = 1

    ship_position = [[],[],[],[],[],[]]
    ship_direction = ["up", "left"]
    
    #hasta llegar a los 6, ejecutar
    while ships_placed != ships:
        while ship_4 > 0:
            #la idea es agarrar una posicion inicial y dirección y crear el array de posiciones basado en longitud de ships
            random_position = [random.randint(0,rows - 4), random.randint(3,cols - 1)]
            random_direction = random.choice(ship_direction)
            if not random_position in ship_position: 
                if random_direction == 'up':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [1,0])))
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [2,0])))
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [3,0])))
                    ship_4 -= 1
                elif random_direction == 'left':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,1])))
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,2])))
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,3])))
                    ship_4 -= 1
            else: 
                ship_4 -= 0
        ships_placed += 1
        while ship_3 > 0:
            random_position = [random.randint(0,rows - 3), random.randint(2,cols - 1)]
            random_direction = random.choice(ship_direction)
            if not random_position in ship_position: 
                if random_direction == 'up':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [1,0])))
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [2,0])))
                    ship_3 -= 1
                    ships_placed += 1
                elif random_direction == 'left':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,1])))
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,2])))
                    ship_3 -= 1
                    ships_placed += 1
            else: 
                ship_3 -= 0        
        while ship_2 > 0:
            random_position = [random.randint(0,rows - 2), random.randint(1,cols - 1)]
            random_direction = random.choice(ship_direction)
            if not random_position in ship_position:
                if random_direction == 'up':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x + y for (x, y) in zip(random_position, [1,0])))
                    ship_2 -= 1
                    ships_placed +=1
                elif random_direction == 'left':
                    ship_position[ships_placed].append(random_position)
                    ship_position[ships_placed].append(list(x - y for (x, y) in zip(random_position, [0,1])))
                    ship_2 -= 1
                    ships_placed +=1
            else: 
                ship_2 -= 0
    # test = []
    # test.append([x+y for (x,y) in zip([1,0], [1,0])])
    # print(test)
   


    #Test of the position
    print(ships_placed)
    print(ship_position)

#location del ship
def place_ship():

    global board
    global ship_position

    for i in ship_position:
        for x in i:
            board[x[0]][x[1]] = '#'
    
    print(board)

# Determinar los indices en el tablero 
def  index_config(rows, cols):

    global board
    global ship_position
    global abc

    input_coord = input().upper()
    index_letter = []
    for letter in abc[0:rows]:
       index_letter.append(letter)
    print(index_letter)

    index_board = []

    if input_coord[0] in index_letter:
        index_board = [index_letter.index(input_coord[0]), int(input_coord[1])]
    else:
        print('Write one possible coordinate')
        
    
    print(index_board)
    
    for x in ship_position:
        for y in x:
            if index_board in x:
                print('Shoot it')

randomly_ships_position(rows,cols)
create_board(rows, cols)
place_ship()
index_config(rows, cols)


