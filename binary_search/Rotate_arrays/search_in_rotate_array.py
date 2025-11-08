class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first , last = 0, len(nums) -1 
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[first] <= nums[mid]: # Left side of array is sorted
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:                       # right side of array is sorted 
                if nums[mid] < target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
        return -1 
        

# brute force solution 
# Linear Search