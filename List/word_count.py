def word_count(list):
    count = 0
    for word in list:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1 
    return count
print(word_count(['abc','aba','121']))

'''
Count Strings with Same Start and End

Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''