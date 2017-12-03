import random

def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p

def swap(matrix, dobutok):
    for i in range(N):
        for j in range(N-1):
            if dobutok[j]>dobutok[j+1]:
                temp = dobutok[j]
                dobutok[j] = dobutok[j+1]
                dobutok[j+1] = temp
                for k in range(N):
                    tmp = matrix[j][k]
                    matrix[j][k] = matrix[j+1][k]
                    matrix[j+1][k] = tmp
    print()
    for i in range(N):
        print(matrix[i],end='')
        print(' |',dobutok[i])

N = int(input("Розмір матриці:"))
matrix, dobutok = [],[]

for i in range(N):
    element = []
    for j in range(N):
        element.append(random.randint(1,3))  #матриця
        #print("%3d" % element[j], end='')
    matrix.append(element)
    print(matrix[i], end='')
    dobutok.append(prod(element)) #добутки
    print(' |', prod(element))
 
swap(matrix,dobutok)


