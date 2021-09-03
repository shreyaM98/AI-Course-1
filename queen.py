
class queen:
    def __init__(self,id, x, y, weight):
        self.id = id
        self.x = x
        self.y = y
        self.weight = weight

    def __repr__(self):
        return '('+ str(self.x) + ', ' + str(self.y) + ')' +'\n'
#check how many queens is a queen attacking
    def is_attacking(self, queen):
        if self.id == queen.id:
            return False
        elif self.x == queen.x:
            return True
        elif self.y == queen.y:
            return True
        elif abs(self.x - queen.x) == abs(self.y - queen.y):
            return True
        else:
            return False
