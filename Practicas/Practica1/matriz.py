import time
from random import randint
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import threading

class MatrizS:
    def __init__(self) -> None:
        pass


    def multiplicacion(self,X,Y):
        
        if len(X[0]) != len(Y):
            return 'Error dimensiones {} != {}'.format(len(X[0]),len(Y))
        else:
            result = [[0 for x in range(len(Y[0]))] for y in range(len(X))] 
            for i in range(len(X)):
                for j in range(len(Y[0])):
                    for k in range(len(Y)):
                        result[i][j] += X[i][k] * Y[k][j]
            
            return result

class MatrizC:
    
    
    def __init__(self) -> None:
        pass

    def mult(self,X,Y,fila,result):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[fila][j] += X[fila][k] * Y[k][j]
    

    def multiplicacion(self,hilos,X,Y):
       
        theads = []
        w  = len(X[0])
        h = len(Y)
        if w != h:
           return 'Error dimensiones {} != {}'.format(w,h)
        else:
            result = [[0 for x in range(len(Y[0]))] for y in range(len(X))] 
            for i in range(len(X)):
                t  = threading.Thread(target= self.mult , args=(X,Y,i,result))
                theads.append(t)
                t.start()

                if hilos == len(theads):
                    for h in theads:
                        h.join()
                    theads.clear()

            for h in theads:
                h.join()
            theads.clear()
            return result
        



if __name__ == '__main__':

    matrices = [10,100,1000]
    hilos = [1,5,10,100]
    tiempo = []
    promedioC = {}
    promedioS = {}

   
    for n in matrices:
        x = [[randint(1,100) for x in range(n)] for y in range(n)] 
        y = [[randint(1,100) for x in range(n)] for y in range(n)] 
        for h in hilos:
            for t in range(20):
                begin_time = time.time()
                MatrizC().multiplicacion(h,x,y)
                tiempo.append(time.time() - begin_time)
            promedioC['{}'.format(h)] = statistics.mean(tiempo)
            print('n={}, h={}'.format(n,h))
            tiempo.clear()
        '''
        for t in range(20):
            begin_time = time.time()
            MatrizS().multiplicacion(x,y)
            tiempo.append(time.time() - begin_time)
        promedioS['{}'.format(n)] = statistics.mean(tiempo)
        tiempo.clear()
        '''

    df  = pd.DataFrame(promedioC, index = matrices)

    df.plot(kind = 'bar')
    plt.show()