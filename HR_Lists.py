'''
Author: Anshul Saboo
Date: 31/03/2021
Problem: HR_Lists
Platform: HackerRank

'''
# Taking input n for count of commands
n = int(input())
output_list = []

#iterating the command line for n times
for _ in range(n):
    inp_string = input().split()
    if inp_string[0] == "append":
        output_list.append(int(inp_string[1]))
    elif inp_string[0] == "insert":
        output_list.insert(int(inp_string[1]), int(inp_string[2]))
    elif inp_string[0] == "remove":
        output_list.remove(int(inp_string[1]))
    elif inp_string[0] == "reverse":
        output_list.reverse()
    elif inp_string[0] == "pop":
        output_list.pop()
    elif inp_string[0] == "sort":
        output_list.sort()
    elif inp_string[0] == "print":
        print(output_list)