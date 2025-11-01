
from sys import stdin

def linearSearch(arr, n, val) :
    for i in range(len(arr)):
        if arr[i] == val:
            return i 
            break
    return -1
    

