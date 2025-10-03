#User function Template for python3

class Solution:
    def findMax(self, N):
        return "".join(sorted(N,reverse = True))


# if they will said to sort a number but they will give in a string means just 
# "".join(sorted(variable))
# if they said to reverse same syntax with extra "".join(sorted(variable,reverse=True))
# gfg