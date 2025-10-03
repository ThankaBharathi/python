
'''
s = "bbbbbbb"
lis = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for char in s:
    if char in lis:
        count += 1
print(count)
'''

s = "Hello World"
count = sum(1 for char in s if char.lower() in 'aeiou')
print(count)


# count the vowels 