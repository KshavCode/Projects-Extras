import numpy as np 
import random 

class MapGenerator :
    def __init__(self, rowsize=10, columnsize=10):
        self.row = rowsize
        self.column = columnsize
        self.map = np.zeros((self.row, self.column), dtype=int)
        self.total_mines = (random.randint(7, 15)*self.row*self.column)//100
        self.mineLocation = []
        self.safetiles = self.row*self.column-self.total_mines
        for _ in range(self.total_mines) :
            i = random.randint(0, self.row-1)
            j = random.randint(0, self.column-1)
            self.map[i][j] = -1
            self.mineLocation.append((i, j))

        for i in range(self.row) :
            for j in range(self.column) : 
                if self.map[i][j] == -1 :
                    # i, j+1 = R            if j+1 < self.column
                    # i, j-1 = L            if j-1 >= 0
                    # i+1, j = D            if i+1 < self.row 
                    # i-1, j = U            if i-1 >= 0
                    # i-1, j-1 = UL         if i and j >=0
                    # i-1, j+1 = UR         if i>=0 and j+1<self.column
                    # i+1, j-1 = DL         if i+1<self.row and j>=0
                    # i+1, j+1 = DR
                    if j+1<self.column and self.map[i][j+1]!=-1 : self.map[i][j+1] += 1    # R
                    if j-1>=0 and self.map[i][j-1]!=-1 : self.map[i][j-1] += 1        # L
                    if i+1<self.row and self.map[i+1][j]!=-1 : self.map[i+1][j] += 1       # D
                    if i-1>=0 and self.map[i-1][j]!=-1 : self.map[i-1][j] += 1        # U
                    if i>0 and j>0 and self.map[i-1][j-1]!=-1 : self.map[i-1][j-1] += 1
                    if i>0 and j+1<self.column and self.map[i-1][j+1]!=-1 : self.map[i-1][j+1] += 1
                    if i+1<self.row and j>0 and self.map[i+1][j-1]!=-1 : self.map[i+1][j-1] += 1
                    if i+1<self.row and j+1<self.column and self.map[i+1][j+1]!=-1 : self.map[i+1][j+1] += 1
      

if __name__=="__main__" :
    obj = MapGenerator()
    print(obj.map)