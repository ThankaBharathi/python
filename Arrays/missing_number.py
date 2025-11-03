class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        for i in range(1,n+1):
            found = False
            for num in arr:
                if num == i:
                    found = True
                    break
            if not found:
                return i
                
        
   