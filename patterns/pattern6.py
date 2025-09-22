n = int(input())
for row in range(1,n+1):
    for cols in range(1,n-(row-1)+1):
        print(cols,end="")
    print()


'''
   12345
   1234
   123
   12
   1
'''