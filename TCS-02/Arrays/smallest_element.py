def find_smallest(arr):
    smallest = arr[0]
    
    for num in arr:
        if num < smallest:
            smallest = num
    
    return smallest

n = int(input())

if n <= 0:
    print("Invalid Input! ")
else:
    
    arr = list(map(int, input().split()))
    
    if len(arr) != n:
        print("Enter a valid number")
     
    else:
        print(find_smallest(arr))
            