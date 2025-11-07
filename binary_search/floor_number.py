class Solution:
    def findFloor(self, arr, x):
        left, right = 0, len(arr)-1
        floor_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                floor_index = mid
                left = mid + 1
            else:
                right = mid - 1
        return floor_index

            
        
        