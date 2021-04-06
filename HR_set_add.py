'''
Author: Anshul Saboo
Date: 06/04/2021
Problem: HR_Set add
Platform: HackerRank

'''
# The set add() method adds a given element to a set if the element is not present in the set
n = int(input())

# Declared empty set
dist_set = set()

for _ in range(n):
    dist_set.add(input())

print(len(dist_set))