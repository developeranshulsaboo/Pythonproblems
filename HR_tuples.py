'''
Author: Anshul Saboo
Date: 31/03/2021
Problem: HR_Lists
Platform: HackerRank

'''
# n = int(input())

#Map function is used to convert every input into int iteratively
integer_list = map(int, input().split())

t = tuple(integer_list)
print(hash(t))