'''
Author: Anshul Saboo
Date: 28/03/2021
Problem: HR_Runner Up Score
Platform: HackerRank

'''
n = int(input())

# Creating an array and simultaneosuly taking input and splitting the string and converting string to int
listArray = map(int, input().split())

#Sorted function will give the value from list on index -2
# List function will convert the array to list
# Set function will generate the random shuffled list
x = (sorted(list(set(listArray)))[-2])

print(x)