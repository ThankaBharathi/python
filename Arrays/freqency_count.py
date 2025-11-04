class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        for i in range(n):
            arr[i] -= 1
        for i in range(n):
            index = arr[i] % n
            arr[index] += n
        for i in range(n):
            arr[i] = arr[i] // n
        return arr
            
    
    
class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = []
        for i in range(1,n+1):
            count = 0
            for num in arr:
                if num == i:
                    count += 1
            freq.append(count)
            
        return freq
        
        