import random
from queen import queen

#class board is a board of queens
class board:
    def __init__(self,id,list_of_queens, dimension):
      self.id = id
      self.cost = 0
      self.list_of_queens = list_of_queens
      self.initial_queens = None
      self.dimension = dimension
      self.hireistic_flag = False

#represents a board by list of queens on the board
    def __repr__(self):
        return str(self.list_of_queens)
#update the board cost
    def update_cost(self):
        attack_cost = 100 * attacking_pairs(self)
        movement_cost = movement_penalty(self.initial_queens,self.list_of_queens)
        self.cost =  attack_cost + movement_cost
#to always have a initial set of queens, that can be used to compare the moved queen
    def initialize(self):
        self.initial_queens = []
        for q in self.list_of_queens:
            self.initial_queens.append(queen(q.id,q.x,q.y,q.weight))
        self.cost = (100 * attacking_pairs(self))
#moves a random queen to a new x,y
    def move_a_random_queen(self):
        queen_pick = random.randint(0,len(self.list_of_queens)-1)
        queen = self.list_of_queens[queen_pick]
        old_x = queen.x
        old_y = queen.y
        new_x = queen.x
        new_y = queen.y

        coordinate_pick  = random.randint(1, self.dimension*2)
        if coordinate_pick < self.dimension:
            new_y = coordinate_pick
        else:
            new_x = coordinate_pick - self.dimension

        # print("Queen Selected:",queen," to be moved at: ",new_x,new_y," with weight: ",queen.weight)
        # print("\n")
         #new pose not the same as current queen pose
        if (queen.x != new_x) or (queen.y != new_y):
            #new pose occupied by an other queen
            if check_if_pos_taken([new_x,new_y],self.list_of_queens) == True:
                self.move_a_random_queen()
            if check_if_pos_taken([new_x,new_y],self.list_of_queens) == False:
                self.list_of_queens[queen_pick].x = new_x
                self.list_of_queens[queen_pick].y = new_y
#Hireistic to improve performance of genetic algo
             # if self.hireistic_flag is True #initialized in genetic.py, if true hireritic is used
                old_cost =  self.cost
                self.update_cost()
                new_cost = self.cost
                if new_cost > old_cost:
                    self.list_of_queens[queen_pick].x = old_x
                    self.list_of_queens[queen_pick].y = old_y
                    self.move_a_random_queen()
        else:
            self.move_a_random_queen()

    def create_new_board(self,id):
        initial_queens = []
        for q in self.list_of_queens:
            initial_queens.append(queen(q.id,q.x,q.y,q.weight))
        new_board = board(id,initial_queens, self.dimension)
        new_board.initialize()
        new_board.move_a_random_queen()
        return new_board

    def merge_boards(self,board):
        list_of_queens1 = self.list_of_queens[:len(self.list_of_queens)//2] + board.list_of_queens[len(board.list_of_queens)//2:]
        queens = []
        for q in list_of_queens1:
            queens.append(queen(q.id,q.x,q.y,q.weight))
        self.list_of_queens = queens
        self.update_cost()

#calculate penalty for miving to new x,y
def movement_penalty(initial_queens,list_of_queens):
    penalty = 0
    for q in initial_queens:
        for u in list_of_queens:
            if q.id == u.id:
                if (q.x != u.x) or (q.y != u.y): #queen has moved
                    steps_moved = abs(q.x - u.x) + abs(q.y - u.y)
                    penalty= penalty + (steps_moved * (u.weight*u.weight))

    return penalty
#calculate number of attacking queens on a board
def attacking_pairs(board):
    attacking_queens = 0
    for q1 in board.list_of_queens:
        for q2 in  board.list_of_queens:
            if q1.is_attacking(q2):
                attacking_queens = attacking_queens +1
    return attacking_queens/2

#check if new position tp be moved at is already occupied by another queen
def check_if_pos_taken(pose, list_of_queens):
    queen_check = False
    for q in list_of_queens:
        # print(pose[0],pose[1])
        if q.x == pose[0] and q.y == pose[1]:
            queen_check = True
    return queen_check
