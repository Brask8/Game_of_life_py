import numpy as np 
import random
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import time

#adding labels to axis

#initializing variables
board_x_nb = 10
board_y_nb = 10
black_case = [] 
black_case_nb = 35
cmap = ListedColormap(['white', 'black'])
life_cycles = 10

def next_turn(board):
    #copy of the board filled with 0 to avoid changing the original board
    new_board = np.zeros((board_x_nb,board_y_nb), dtype=int)

    #checking the number of black cases around each case
    for i in range(board_x_nb):
        for j in range(board_y_nb):
            neighbours = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            black_neighbours = 0
            for k in range(8):
                try:
                    if board[neighbours[k]] == 1:
                        black_neighbours += 1
                except IndexError:
                    pass

            #applying the rules of the game    
            if board[i,j] == 0 and black_neighbours == 3:
                new_board[i,j] = 1

            elif board[i,j] == 1 and 2<black_neighbours<4:
                new_board[i,j] = 1
            else :
                new_board[i,j] = 0

    return new_board
    time.sleep(3)

#generating a 10x10 matrix of 0
print("Test board : ")
board = np.zeros((board_x_nb,board_y_nb), dtype=int)
# board[1::2, ::2] = 1
# board[::2, 1::2] = 1

#generating random black cases
for i in range(black_case_nb):
    m = random.randint(0,9)
    n = random.randint(0,9)
    black_case.append([m,n])

print(black_case)
#print(board, "\n")

#filling the matrix with black cases and printing it
for indices in black_case:
    board[indices[0], indices[1]] = 1
#print(board)
plt.matshow(board, cmap=cmap)
plt.show()

for i in range(life_cycles):
     board = next_turn(board)
     plt.matshow(board, cmap=cmap)
     plt.show()