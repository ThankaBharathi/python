def min_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(min_list([1,2,3,4,5,-9,-10]))

# Get Smallest Number in List
#Write a Python program to get the smallest number from a list.