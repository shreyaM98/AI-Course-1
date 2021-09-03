
import numpy as np
from queen import queen
from board import board
from genetic import populate_generation
import matplotlib.pyplot as plt



def read_board_csv(filename):
    board_configuration_2d = np.genfromtxt(filename, delimiter=',')
    list_of_queens = []
    queen_id = 1
    for i in range(board_configuration_2d.shape[0]):
        for j in range(board_configuration_2d.shape[0]):
            if board_configuration_2d[j,i] != 0:
                list_of_queens.append(queen(queen_id, i+1, j+1, board_configuration_2d[j,i]))
                queen_id = queen_id + 1

    return board(1,list_of_queens,board_configuration_2d.shape[0])


#run File

# (boardsize, <population size>, <# of generations>, <elitism %>, <crosover %>, <mutation %>
populate_generation(read_board_csv('board_8x8.csv'),800,1000,20,40,40)


# plt.scatter(x, y)
# plt.show()

# print("--- %s seconds ---" % (time.time() - start_time))
# #end
