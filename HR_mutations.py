'''
Author: Anshul Saboo
Date: 02/04/2021
Problem: HR_Mutations
Platform: HackerRank

'''

def mutate_string(string, position, character):
    l = list(string) #convert string to list
    l[position] = character #change the character in list for specific position
    string = "".join(l) # use join to convert list to string
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)