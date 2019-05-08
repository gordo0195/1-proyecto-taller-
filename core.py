import random

###########Parte 1 funcion que asigna un numero aleatorio entre 2 y 4 a cada posición de la matriz que no esté ocupada######
matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def asigna():
    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    n=0;y=0
    new=[]
    return asigna_aux(matriz, n, y, new)

def asigna_aux(matriz, n, y, new):
    if n == 0:
        if y < len(matriz[n])-1:
            if int(matriz[n][y]) == 0:
                matriz[n][y] = random.randint(0,1)
                if matriz[n][y]==0:
                    matriz[n][y] = 2
                elif matriz[n][y]==1:
                    matriz[n][y] = 4
                print(matriz[0],'\n',matriz[1], '\n', matriz[2],'\n')
                return asigna_aux(matriz, n, y+1, new)
            else:
                return asigna_aux(matriz, n, y+1, new)
            
        elif y == len(matriz[n])-1:
            if int(matriz[n][y]) == 0:
                matriz[n][y] = random.randint(0,1)
                if matriz[n][y]==0:
                    matriz[n][y] = 2
                elif matriz[n][y]==1:
                    matriz[n][y] = 4
                print(matriz[0],'\n',matriz[1], '\n', matriz[2],'\n')
                return asigna_aux(matriz, n+1, 0, new)
            else:
                return asigna_aux(matriz, n+1, 0, new)
        else:
            return asigna_aux(matriz, n+1, 0, new)
    
    elif n <= len(matriz)-1:
        if y < len(matriz[n])-1:
            if int(matriz[n][y]) == 0:
                matriz[n][y] = random.randint(0,1)
                if matriz[n][y]==0:
                    matriz[n][y] = 2
                elif matriz[n][y]==1:
                    matriz[n][y] = 4
                print(matriz[0],'\n',matriz[1], '\n', matriz[2],'\n')
                return asigna_aux(matriz, n, y+1, new)
            else:
                return asigna_aux(matriz, n, y+1, new)
            
        elif y == len(matriz[n])-1:
            if int(matriz[n][y]) == 0:
                matriz[n][y] = random.randint(0,1)
                if matriz[n][y]==0:
                    matriz[n][y] = 2
                elif matriz[n][y]==1:
                    matriz[n][y] = 4
                print(matriz[0],'\n',matriz[1], '\n', matriz[2],'\n')
                return asigna_aux(matriz, n+1, 0, new)
            else:
                return asigna_aux(matriz, n+1, 0, new)
                  
#Ver sumas
def asigno(matriz):
    i=random.randint(0,3)
    j=random.randint(0,3)
    if matriz[i][j] == 0:
        matriz[i][j] = random.randint(0,1)
        if matriz[i][j]==0:
            matriz[i][j] = 2
            print(matriz[0], '\n', matriz[1], '\n', matriz[2],'\n', matriz[3])
        elif matriz[i][j]==1:
            matriz[j][j] = 4
            print(matriz[0], '\n', matriz[1], '\n', matriz[2],'\n', matriz[3])
        else:
            return asigno(matriz)
    else:
        return asigno(matriz)

def cuadrícula():
    for i in range(0,3):
        for j in range(0,3):
            cell=0
            print(cell)
            j+=1
        i+=1
    print(cell)

    
    
