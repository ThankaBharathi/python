def reverse_arr(arr):
    first, last = 0, len(arr)-1
    
    while first <= last:
        arr[first], arr[last] = arr[last],arr[first]
        first += 1
        last -= 1
    
    return arr

arr = [1,2,3,4,5]
print(reverse_arr(arr))