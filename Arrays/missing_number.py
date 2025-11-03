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
                
        
class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        xor_num = 0
        xor_arr = 0
        for i in range(1,n+1):
            xor_arr ^= i
        for num in arr:
            xor_num ^= num
        return xor_arr ^ xor_num
        
                
        
   