def largest_smallest(arr):
    
    smallest = largest = arr[0]
    
    for num in arr:
        if smallest > num:
            smallest = num
        
        if largest < num:
            largest = num
    
    return smallest, largest

n = int(input())

if n <= 0:
    print("Invalid Input")

else:
    arr = list(map(int, input().split()))
    
    if len(arr) != n:
        print("Enter the invalid number")
    
    else:
        print(largest_smallest(arr))