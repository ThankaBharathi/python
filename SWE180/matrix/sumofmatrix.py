
#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        total = 0
        for i in range(N):
            for j in range(M):
                total += Grid[i][j]
        return total

# in this problem add the sum using 
# N rows and M cols 
'''
total = 0
for i in range(N): # outer loop is run for row times 
    for j in range(M): # inner loop is run for cols times
        total += Grid[i][j]
    return total

# why means different rows and cols so we will add as rows and cols 

'''
Grid = [  this is 2 x 3 matrix 
    [1,2,3],
    [2,3,4]
]

'''
'''