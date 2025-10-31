class Solution:
    def isSorted(self, arr) -> bool:
        if_sorted = True
        for i in range(len(arr) -1):
            if arr[i] >arr[i+1]:
                if_sorted = False
                break
        return if_sorted
        
        