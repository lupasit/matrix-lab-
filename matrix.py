#linear algebra\линал
def createMatrix(row:int,col:int)->list[list]:
    matrix = [[0 for i in range(col)] for j in range(row)]
    return matrix
crMt = createMatrix
def createEdentityMatrix(row:int,col:int)->list[list]:
    matrix = [[1 if i==j else 0 for i in range(col)] for j in range(row)]
    return matrix
edentity = createEdentityMatrix
def simpelFindDet3x3(A:list[list])->float:
    det = ((A[0][0] * A[1][1] * A[2][2])
           + (A[0][1] * A[1][2] * A[2][0])
           + (A[0][2] * A[1][0] * A[2][1])
           - (A[0][2] * A[1][1] * A[2][0])
           - (A[0][0] * A[1][2] * A[2][1])
           - (A[0][1] * A[1][0] * A[2][2]))
    return det
# simpleFindDet3x3 Находит определитель матрицы 3 на 3 по правилу Саррюса (треугольники)
# нет обработчика ошибок
def minor3x3(matrix,i:int,j:int): #row - строка col - столбец
   matrix_minor = [
       [matrix[row][col] for col in range(3) if col !=j]
       for row in range(3) if row !=i
   ]
   det_minor = matrix_minor[0][0] * matrix_minor[1][1] - matrix_minor[0][1] * matrix_minor[1][0]
   return det_minor
# minor3x3 принимает матрицу 3X3 и строку со столбцом и находит матрицу миноров
# нет обработчика ошибок
def findMinorDet3x3(A):
    det =(A[0][0]*minor3x3(A,0,0)
          - A[0][1]*minor3x3(A,0,1)
          + A[0][2]*minor3x3(A,0,2))
    return det
# принимает матрицу 3х3 и методом алгебраических дополнений
# нет обработчика ошибок
def addMatrix(A,B):
    if len(A) != len(B):
        return -1
    if len(A[0]) != len(B[0]):
        return -1
    rows = len(A)
    cols = len(A[0])
    add = []
    for i in range(rows):
        low_res = []
        for j in range(cols):
            res = A[i][j] + B[i][j]
            low_res.append(res)
        add.append(low_res)
    return add
addM = addMatrix
# addMatrix складывает матрицы одинаковых размеров
# нет обработчика ошибок
def bruceMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j],end=" ")
        print()
print_mat = bruceMatrix
# bruceMatrix выводит матрицу в ее виде, не строкой
def subMatrix(A,B):
    if len(A) != len(B):
        return -1
    if len(A[0]) != len(B[0]):
        return -1
    rows = len(A)
    cols = len(A[0])
    sub = []
    for i in range(rows):
        low_res = []
        for j in range(cols):
            res = A[i][j] - B[i][j]
            low_res.append(res)
        sub.append(low_res)
    return sub
subM = subMatrix
# sudMatrix принимает матрицы и вычитает их
# нет обработчика ошибок
def transposeMatrix(A:list[list])-> list[list]:
    return [list(row) for row in zip(*A)]
transposeM = transposeMatrix
# transposeMatrix принимает матрицу и выдает ее транспорнированную версию
# нет обработчика ошибок
def inversMatrix(A:list[list])-> list[list]:
    minor_det = findMinorDet3x3(A)
    if minor_det == 0:
        return -1
    rows = len(A)
    cols = len(A[0])
    minorMatrix = []
    for i in range(rows):
        low_res = []
        for j in range(cols):
            res = minor3x3(A,i,j)
            low_res.append(res)
        minorMatrix.append(low_res)
    algcomMatrix = []
    for i in range(rows):
        low_res1 = []
        for j in range(cols):
            res1 = (-1)**(i+j+2) * minorMatrix[i][j]
            low_res1.append(res1)
        algcomMatrix.append(low_res1)
    transMatrixAlgCom= transposeMatrix(algcomMatrix)
    invMatrix = []
    for i in range(rows):
        low_res2 = []
        for j in range(cols):
            low_res2.append(transMatrixAlgCom[i][j] / minor_det)
        invMatrix.append(low_res2)

    return invMatrix
invM = inversMatrix
# inversMatrix принимает только матрицу 3х3 и возвращает ее обратную
# нет обработчика ошибок
def universalMinor(matrix:list[list],row:int,col:int) -> list[list]:
    res =[]
    for i in range(len(matrix)):
        if i == row:
            continue
        new_row = []
        for j in range(len(matrix)):
            if j == col:
                continue
            new_row.append(matrix[i][j])
        res.append(new_row)
    return res
findMinor = universalMinor
# universalMinor вычисляет минор для матриц любых размеров
# нет обработчика ошибок
def simpleFindDet2x2(matrix:list[list])-> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
# simpleFindDet2x2 принимает матрицу и вычисляет ее определитель
# нет обработчика ошибок
def universalDet(matrix:list[list])-> float:
    n = len(matrix)
    if n == 0:
        return -1
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return simpleFindDet2x2(matrix)
    det1 = 0
    for j in range(n):
        minor = universalMinor(matrix,0,j)
        det1 += (
        (-1)**(j) * matrix[0][j]
        * universalDet(minor)
        )
    return det1
findDet = universalDet
# universalDet принимает матрицу любого размера и возвращает ее определитель способом алгебраических дополнений
# нет обработчика ошибок
def multiMatrix(A:list[list],B:list[list])-> list[list]:
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    res = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                res[i][j] += A[i][k] * B[k][j]
    return res
multiM = multiMatrix
def cramer(A,B):
    det_A = universalDet(A)
    if det_A == 0:
        raise ValueError("Determinant == 0")
    n = len(A)
    x = []
    for i in range(n):
        A_i = []
        for row_idx in range(n):
            new_row = list(A[row_idx])
            new_row[i] = B[row_idx]
            A_i.append(new_row)
        det_Ai = universalDet(A_i)
        x.append(det_Ai/det_A)
    return x
def matrixRotateRad(A:list[list],radX:float,radY:float,radZ:float,x:str)-> list[list]:
    n = len(A)
    an = len(A[0])
    if n == 0:
        return -1
    if n == 1:
        return -2
    if (n == 2) and (an == 1):
        C = [
            [rcos(radX),-rsin(radX)],
            [rsin(radX),rcos(radX)]
        ]
        return multiMatrix(C,A)
    elif ((n == 3) and (an == 1) and (x == "x")):
        C = [
            [1,0,0],
            [0,rcos(radX),-rsin(radX)],
            [0,rsin(radX),rcos(radX)]
        ]
        return multiMatrix(C,A)
    elif (n == 3) and (an == 1) and (x == "y"):
        C = [
            [rcos(radY),0,rsin(radY)],
            [0,1,0],
            [-rsin(radY),0,rcos(radY)]
        ]
        return multiMatrix(C,A)
    elif (n == 3) and (an == 1) and (x == "z"):
        C = [
            [rcos(radZ),-rsin(radZ),0],
            [rsin(radZ),rcos(radZ),0],
            [0,0,1]
        ]
        return multiMatrix(C,A)
rotateRad = matrixRotateRad
def matrixRotateDeg(A:list,angX:float,angY:float,angZ:float,x:str)-> list[list]:
    n = len(A)
    an = len(A[0])
    radX = degtorad(angX)
    radY = degtorad(angY)
    radZ = degtorad(angZ)
    if n == 0:
        return -1
    if n == 1:
        return -2
    if (n == 2) and (an == 1):
        C = [
            [rcos(radX),-rsin(radX)],
            [rsin(radX),rcos(radX)]
        ]
        return multiMatrix(C,A)
    elif ((n == 3) and (an == 1) and (x == "x")):
        C = [
            [1,0,0],
            [0,rcos(radX),-rsin(radX)],
            [0,rsin(radX),rcos(radX)]
        ]
        return multiMatrix(C,A)
    elif (n == 3) and (an == 1) and (x == "y"):
        C = [
            [rcos(radY),0,rsin(radY)],
            [0,1,0],
            [-rsin(radY),0,rcos(radY)]
        ]
        return multiMatrix(C,A)
    elif (n == 3) and (an == 1) and (x == "z"):
        C = [
            [rcos(radZ),-rsin(radZ),0],
            [rsin(radZ),rcos(radZ),0],
            [0,0,1]
        ]
        return multiMatrix(C,A)
rotateDeg = matrixRotateDeg
def addElement(matrix:list[list],i:int,j:int,element:float)->list[list]:
    matrix[i][j] = element
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
    def classfindDet(self):
        print(findDet(self.data))
    def edentity(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i==j:
                    self.data[i][j] = 1
                else:
                    self.data[i][j] = 0
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix not equal")
        res = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix not equal")
        res = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.data[i][j] - other.data[i][j]
        return res
    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Матрицу можно умножить только на другую матрицу")
        if self.cols != other.rows:
            raise ValueError(
                f"Несовпадающие размеры: матрицу {self.rows}x{self.cols} "
                f"нельзя умножить на матрицу {other.rows}x{other.cols}"
            )
        res = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res.data[i][j] += self.data[i][k] * other.data[k][j]
        return res





#mathematical analysis\матанализ
def integrate(f,a,b,n):
    dx = (b-a)/n
    total = 0.0
    for i in range(n):
        x = a + i*dx
        total += f(x) * dx
    return total
#Trigonometry\Тригонометрия
def normalizeRad(x:float)->float:
    return (x+pi)%(2*pi)-pi
def rsin(x:float,k = 20)->float:
    x = normalizeRad(x)
    res = 0
    term = x
    for i in range(k):
        res +=term
        term = (-1)*term * x**2 / ((2*i+2)*(2*i+3))
    return res
def rcos(x:float,k=20)->float:
    x = normalizeRad(x)
    res = 0
    term = 1.0
    for i in range(k):
        res +=term
        term *= -(x*x)/((2 * i + 1)*(2 * i + 2))
    return res
def angcos(x:int)->float:
    angle = degtorad(x)
    return rcos(angle)
def angsin(x:int)->float:
    angle = degtorad(x)
    return rsin(angle)
def degtorad(x):
    return x*pi/180
def radtodeg(x):
    return x*180/pi
def rtan(x):
    return rsin(x)/rcos(x)
def rctx(x):
    return rcos(x)/rsin(x)
#combinatorics\комбинаторика
def factorial(n:int):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)
#const\константы
pi = 3.141592653589793
e = 2.718281828459045
g = 9.81
