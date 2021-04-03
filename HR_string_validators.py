'''
Author: Anshul Saboo
Date: 03/04/2021
Problem: HR_String validator
Platform: HackerRank

'''
# the any function iterate the given input or string
string = input()
print(any(s.isalnum() for s in string)) # alnum checks alphanumeric
print(any(s.isalpha() for s in string)) # alpha checks alphabetics
print(any(s.isdigit() for s in string)) # isdigit checks numbers
print(any(s.islower() for s in string)) # islower checks lower case characters
print(any(s.isupper() for s in string)) # isupper checks upper case characters