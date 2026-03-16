def second_smallest_second_largest(arr):
    smallest = s_small = float('inf')
    largest = s_large = float('-inf')
    
    for num in arr:
        if num < smallest:
            s_small = smallest
            smallest = num
        elif num < s_small and num != smallest:
            s_small = num
        
        if num > largest:
            s_large = largest
            largest = num
        
        elif num > s_large and num != largest:
            s_large = num
        
    
    return s_small, s_large

n = int(input())

if n <= 0:
    print("Invalid Input! ")
else:
    arr = list(map(int, input().split()))
    
    if len(arr) != n:
        print("Enter a valid number")
    else:
        print(second_smallest_second_largest(arr))
    