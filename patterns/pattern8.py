n = int(input())
for row in range(1,n+1):
    for space in range(1,(row-1)+1):
        print(" ",end="")
    for cols in range(1,(2*(n-row)+1)+1):
        print("*",end="")
    print()

'''
    *********
     *******
      *****
       ***
        *
'''