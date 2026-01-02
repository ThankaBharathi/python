def find_smallest_largest(arr):
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


# -------- Input Handling --------
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid input")
else:
    arr = list(map(int, input("Enter elements: ").split()))
    smallest, largest = find_smallest_largest(arr)
    print("Smallest element:", smallest)
    print("Largest element:", largest)
