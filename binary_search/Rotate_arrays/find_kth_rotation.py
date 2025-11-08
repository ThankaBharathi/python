class Solution:
    def findKRotation(self, arr):
        index = 0
        for i in range(len(arr)):
            if arr[i] < arr[index]:
                index = i
        return index
      
        
        
        