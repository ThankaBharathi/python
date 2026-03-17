def summ(arr):
    sum = 0
    for num in arr:
        sum += num
    
    return sum / len(arr)

arr = [1,2,3,4,5]
print(summ(arr))