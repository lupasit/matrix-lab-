import random
import matrix as  mt
A = mt.Matrix(20,20)
A.edentity()
for i in range(A.rows):
    for j in range(A.cols):
        A.set_element(i,j,random.random())
for i in range(A.rows):
    for j in range(A.cols):
        if A.returnElemt(i,j) =