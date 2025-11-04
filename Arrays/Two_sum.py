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


class Solution:
	def twoSum(self, arr, target):
	    arr.sort()
	    found = False
	    first = 0
	    last = len(arr)-1
	    while first < last:
	        current_sum = arr[first] + arr[last]
	        if current_sum == target:
	            return True
	            found = True
	            break
	        elif current_sum < target:
	            first += 1
	        else:
	            last -= 1
	    if not found:
	        return False
	       
	            
	    
	    
	    
		