arr = [1,2,3,4,5]
new = 6

new_arr = [0] * (len(arr)+1)

for i in range(len(arr)):
    new_arr[i] = arr[i]

new_arr[len(arr)] = new

print(new_arr)