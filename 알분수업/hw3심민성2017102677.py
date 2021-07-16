# 2017102677 소프트웨어융합학과 심민성

# quickSort

def quickSort(s, low , high):
    if low < high:
        pivotIdx = partition(s, low, high)
        quickSort(s, low, pivotIdx - 1)
        quickSort(s, pivotIdx + 1 , high)

def partition(s, low, high):
    pivotItem = s[low]
    pivotIdx = low

    for i in range(low + 1, high + 1):
        if s[i] < pivotItem:
            pivotIdx += 1
            s[i], s[pivotIdx] = s[pivotIdx], s[i]
    
    s[pivotIdx] , s[low] = s[low] , s[pivotIdx]
    
    return pivotIdx
    

    
s = [3, 5, 2, 9, 10, 14, 4, 8]

quickSort(s, 0 ,7)
print(s)

print('---------------------------------------------------')

# prod

import math

def prod2(a,b):
    n = max(len(str(a)), len(str(b)))
    
    if a == 0 or b == 0:
        return 0
    
    elif n <= 4:
        return a * b
    
    else:
        m = math.floor(n / 2)
        x = a // pow(10 , m)
        y = a % pow(10 , m)
        w = b // pow(10 , m)
        z = b % pow(10 , m)
        
        r = prod2(x + y , w + z)
        p = prod2(x , w)
        q = prod2(y , z)
    
        return p * pow(10, 2*m) + (r - p - q) * pow(10 , m) + q

a = 1234567812345678
b = 2345678923456789

print(prod2(a , b))
print(a * b)
        
