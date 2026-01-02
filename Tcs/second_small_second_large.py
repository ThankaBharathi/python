def second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None

    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        # For smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        # For largest
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest < num < largest:
            second_largest = num

    if second_smallest == float('inf') or second_largest == float('-inf'):
        return None, None

    return second_smallest, second_largest


# -------- Input Handling --------
n = int(input("Enter number of elements: "))

if n < 2:
    print("Not possible")
else:
    arr = list(map(int, input("Enter elements: ").split()))
    sec_small, sec_large = second_smallest_largest(arr)

    if sec_small is None or sec_large is None:
        print("Not possible")
    else:
        print("Second Smallest:", sec_small)
        print("Second Largest:", sec_large)
