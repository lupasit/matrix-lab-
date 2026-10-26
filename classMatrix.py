import matrix as mt
class Matrix:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.data = [
            [0 for j in range(cols)] for i in range(rows)
        ]
    def show(self):
        for row in self.data:
            print(row)
    def set_element(self,i,j,value):
        self.data[i][j] = value
    def findDet(self):
        print(mt.findDet(self.data))
    def edentity(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i==j:
                    self.data[i][j] = 1
                else:
                    self.data[i][j] = 0



