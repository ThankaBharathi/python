class Solution:
    def findKRotation(self, arr):
        index = 0
        for i in range(len(arr)):
            if arr[i] < arr[index]:
                index = i
        return index
      
        
        
class Solution:
    def findKRotation(self, arr):
        left, right = 0, len(arr) - 1
        
        if arr[left] < arr[right]:
            return 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return mid
    
            if mid < right and arr[mid] > arr[mid + 1]:
                return mid + 1
            
            if arr[left] <= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return 0  
