def find_largest_optimized(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


# -------- Input Handling --------
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid input")
else:
    arr = list(map(int, input("Enter elements: ").split()))
    print("Largest element:", find_largest_optimized(arr))
