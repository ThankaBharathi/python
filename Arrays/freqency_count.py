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
            
    
    
