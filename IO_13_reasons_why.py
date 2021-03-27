'''
Author: Anshul Saboo
Date: 27/03/2021
Problem: IO_Jaddoo and DNA transcryption
Platform: HackerEarth

'''

#Taking three inputs at a time and spliting using split()
a, b, c = input().split()

#converting them into integers
a = int(a)
b = int(b)
c = int(c)

#Swapping a and b
d = a
a = b
b = d

#multiplying a by c and adding b by c
a *= c
b += c

#printing final values of a and b
print(a, b)