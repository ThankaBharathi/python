def largest_element(arr):
    
    largest = arr[0]
    
    for num in arr:
        if largest < num:
            largest = num
    
    return largest

n = int(input())

if n <= 0:
    print("Invalid Input! ")
else:
    arr = list(map(int, input().split()))
    
    if len(arr) != n:
        print("Enter valid number")
    else:
        print(largest_element(arr))
    