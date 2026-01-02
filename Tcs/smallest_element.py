def find_smallest_optimized(arr):
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num

    return smallest


# -------- Input Handling --------
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid input")
else:
    arr = list(map(int, input("Enter elements: ").split()))
    print("Smallest element:", find_smallest_optimized(arr))
