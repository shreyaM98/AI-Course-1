import numpy as np
import pandas as pd


def q_safe(board_1, row, col, qwt):
    # check for attacking queen in the same col
    for i in range(row):
        if board_1[i][col] in qwt:
            return False

    # check for attacking queen in the bottom-right to top-left diagonal
    # for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    #    if board_1[i][j] == 1:
    #        return False

    # check for attacking queen in the top-right to bottom-left diagonal
    # for i, j in zip(range(row, len(board_1), 1), range(col, -1, -1)):
    #    if board_1[i][j] == 1:
    #        return False

    # better way to find the attacking queens in diagonals
    # we use the linear algebra method i.e |x1 - x2| = |y1 - y2|
    # used to check if two points lie on the same line
    for i in range(row):
        for j in range(col):
            if board_1[i][j] in qwt and abs(row - i) == abs(col - j):
                return False

    return True


def q_solver(board_1, row, qwt):
    if row >= len(board_1):
        return True

    for i in range(len(board_1)):

        if q_safe(board_1, row, i, qwt):
            board_1[row][i] = qwt[row]

            if q_solver(board_1, row + 1, qwt) == True:
                return True

            board_1[row][i] = 0

    return False


def printBoard(board_1, board_2):

    print("####Input Board####")
    board_2 = board_2.tolist()
    for i in range(len(board_2)):
        for j in range(len(board_2)):
            print(board_2[i][j], end=" ")
        print()

    print("\n####Optimal Board####")
    for i in range(len(board_1)):
        for j in range(len(board_1)):
            print(board_1[i][j], end=" ")
        print()


def compareBoard(board_1, board_2):

    board_1 = np.array(board_1[:])
    board_1 = np.transpose(board_1)
    q_pos_1 = board_1.flatten()
    q_pos_1 = q_pos_1.tolist()
    q_pos_1 = [i for i in q_pos_1 if i != 0]

    board_2 = np.transpose(board_2[:])
    q_pos_2 = board_2.flatten()
    q_pos_2 = q_pos_2.tolist()
    q_pos_2 = [i for i in q_pos_2 if i != 0]

    total_cost = 0
    for i in range(len(q_pos_1)):
        for j in range(len(q_pos_2)):
            if q_pos_1[i] == q_pos_2[j]:
                tiles_moved = abs(i - j)
                cost = tiles_moved * (q_pos_1[i] ** 2)
                total_cost = total_cost + cost

    return total_cost


def solveBoard():

    row = 7
    col = 7
    board_1 = np.zeros((row, col), dtype=int).tolist()

    # queen weights
    qwt = [1, 2, 3, 4, 5, 6, 7]

    if q_solver(board_1, 0, qwt) == False:
        print("solution does not exist")
        return False

    board_2 = pd.read_csv("board.csv", sep=",", header=None)
    board_2 = board_2.to_numpy()

    printBoard(board_1, board_2)

    cost = compareBoard(board_1, board_2)
    print("\ncost is: ", cost)

    return True


solveBoard()