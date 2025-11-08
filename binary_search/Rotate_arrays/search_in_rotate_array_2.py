class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        first , last = 0, len(nums)-1
        while first <= last:
            mid = (first + last) // 2
            
            if nums[mid] == target:
                return True
            # case 1 if left right and mid are same elements

            if nums[first] == nums[mid] == nums[last]:
                first += 1
                last -= 1
            # Left half sorted
            elif nums[first] <= nums[mid]:
                if nums[first] <= target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] < target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
        return False


# same as rotate array 1 this problem have duplicates for that we are using one condition 
# brute force solution is Linear search 