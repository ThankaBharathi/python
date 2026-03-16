def reverse_array_optimized(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# -------- Input Handling --------
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid input")
else:
    arr = list(map(int, input("Enter elements: ").split()))
    result = reverse_array_optimized(arr)
    print("Reversed array:", *result)
