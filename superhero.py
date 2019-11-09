import sys
import numpy as np

try:
    supe = [int(x) for x in input("Please input the heroes' power: ").split()]
    nb_of_switches = int(input("Please input the number of power flips: "))
    if nb_of_switches > len(supe) or nb_of_switches < 0:
        print("Sorry, this is not a valid number of power flips.")
except (ValueError):
    print("Sorry, these are not valid power values.")
    sys.exit()

def summation(arr):
    summa = 0
    for i in arr:
        summa = summa + i
    return summa

def switches(n):
    supeh = supe[:]
    for i in range(len(supeh)):
        j = supeh.index(min(supeh))
        supeh[i],supeh[j] = supeh[j],supeh[i]
        supeh[i] = supeh[i] * -1
        n = n-1
        if(n==0):
            break
    print("Possibly flipping the power of the same hero many times, the greatest achievable power is",summation(supeh))

def switches_once(n):
    supeh = supe[:]
    add=0
    truth = True
    while(truth):
        for i in supeh:
            j = supeh.index(min(supeh))
            add = add + supeh[j]*-1
            del supeh[j]
            n = n-1
            if(n==0):
                truth = False
                break
    return add + summation(supeh)

def switches_consec(n):        
    supeh = supe[:]
    if(n == len(supeh)):
         add = switches_once(n)
         return add
    else:
        arr = []
        for i in range(len(supeh)-n+1):
            j = supeh[i:i+n]
            arr.append((summation(j)*-2+summation(supeh)))
    return max(arr)

def switches_max():
    supeh = supe[:]
    if(all(i>0 for i in supeh)):
        result= summation(supeh)
    elif(all(i<0 for i in supeh)):
        result= -1 * summation(supeh)
    else:
        arr=[]
        truth = True
        maxi = len(supeh)-1
        while(maxi!=0):
            for i in range(maxi):
                j = supeh[i:i+maxi]
                if(all(i>0 for i in j)):
                    continue
                arr.append((summation(j)*-2)+summation(supeh))
            maxi = maxi - 1
        result = max(arr)
                
    print("Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is", result)#summation(supeh)

    
switches(nb_of_switches)
print("Flipping the power of the same hero at most once, the greatest achievable power is" ,switches_once(nb_of_switches),".")
print("Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is", switches_consec(nb_of_switches),".")
switches_max()
