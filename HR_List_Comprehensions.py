'''
Author: Anshul Saboo
Date: 28/03/2021
Problem: HR_List Comprehensions
Platform: HackerRank

'''
# Taking basic 4 inputs as problem instruction
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Creating a empty list to store the final output
listFinal = []

for i in range(0, x+1): #creating i as index for numbers between 0 to x+1
    for j in range(0, y+1): #creating j as index for numbers between 0 to y+1
        for k in range(0, z+1): #creating k as index for numbers between 0 to z+1
            if (i+j+k != n): # If the sumation of i,j,k is not equal to n then append in list
                listFinal.append([i,j,k])

print(listFinal)

#Detailed working of code in terms of output for input 1 1 1 2
# In the example above, that's what will happen behind the scenes, in this exact order:

# i = 0, j = 0, k = 0

# i = 0, j = 0, k = 1

# i = 0, j = 1, k = 0

# i = 0, j = 1, k = 11


# i = 1, j = 0, k = 0

# i = 1, j = 0, k = 1

# i = 1, j = 1, k = 0

# i = 1, j = 1, k = 1

# It will print exactly like that:

# [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]

# As you can see, it made 8 different output variations.