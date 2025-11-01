class Solution:
    def sort012(self, arr):
        one = two = zero = 0
        for num in arr:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1
        arr[:] = [0]*zero + [1]*one + [2]*two
        return arr
                
                
        
        
        
        