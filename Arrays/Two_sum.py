arr = [0, -1, 2, -3, 8]
target = 2
found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(True)
            found = True
            break
    if found:
        break
if not found:
    print(False)


arr = [0, -1, 2, -3, 8]
target = 5
found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print([i,j])
            found = True
            break
    if found:
        break
if not found:
    print(False)

# optimized 

arr = [0, -1, 2, -3, 8]
target = 5

seen = {}
for i,num in enumerate(arr):
    need = target - num
    if need in seen:
        print([seen[need],i])
        break
    seen[num] = i
print([])
    

    
   
    