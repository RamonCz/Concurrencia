import numpy as np
import threading

class MatrizS:
    def __init__(self) -> None:
        pass
    def multiplicacion(self,X,Y):
        w  = len(X[0])
        h = len(Y)
        if w != h:
            print('Error dimensiones {} != {}'.format(w,h))
        else:
            result = [[0 for x in range(w)] for y in range(h)] 
            for i in range(len(X)):
                for j in range(len(Y[0])):
                    for k in range(len(Y)):
                        result[i][j] += X[i][k] * Y[k][j]

            for r in result:
                print(r)

class MatrizC:
    def __init__(self) -> None:
        pass

    def mult(self,X,Y):
        w  = len(X[0])
        h = len(Y)
        if w != h:
            print('Error dimensiones {} != {}'.format(w,h))
        else:
            result = [[0 for x in range(w)] for y in range(h)] 
            for i in range(len(X)):
                for j in range(len(Y[0])):
                    for k in range(len(Y)):
                        result[i][j] += X[i][k] * Y[k][j]


    def multiplicacion(self,X,Y):
        t1 = threading.Thread(target= mult , args= X,Y)
        t


x = [[1,2,3],[4,5,6]]
y = [[1,2,3],[4,5,6],[7,8,9]]

MatrizS().multiplicacion(x,y)


x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(x.shape)
print(x.dot(y))
