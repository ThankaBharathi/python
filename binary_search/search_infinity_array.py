'''

    def get(i):
    
        Use the given get function which is given as an argument here, 
        that returns the value at index i
        in the infinite sorted binary array.

'''

def firstOne(get):
    index = 1
    while get(index) == 0:
        index *= 2
    ans = -1
    left = index // 2
    right = index

    while left <= right:
        mid = (left + right) // 2
        if get(mid) == 1:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

    
    
    
    
    