#User function Template for python3

class Solution:
    def checkYear (self, n):
        return True if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else False
    
# Leap year means year % 4 and not % by 100 or divided by 400 
# easy problem in gfg
