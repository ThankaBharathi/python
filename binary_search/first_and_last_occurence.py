#User function Template for python3
class Solution:
    def find(self, arr, x):
        left , right, first = 0,len(arr)-1,-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                first = mid
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        left , right, second = 0,len(arr)-1,-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                second = mid
                left = mid + 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return [first, second]
        
        
        
            
