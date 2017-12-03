import numpy
import math

def recur(n,summ, aprev, bprev, k):
    if k <= n:
        acurrent = 0.5*(math.sqrt(bprev)+0.5*math.sqrt(aprev))
        bcurrent = 2*math.pow(aprev,2)+ bprev 
        summ += (acurrent * bcurrent)/math.factorial(k)
        k+=1
        aprev = acurrent
        bprev = bcurrent
        recur(n,summ, aprev, bprev, k)
    else:
        return print(summ)

summ, aprev, bprev, k = 1,1,1,2
print('Задайте натуральне N:')
n = int(input())
res = recur(n,summ, aprev, bprev, k)




