'''
Author: Anshul Saboo
Date: 02/04/2021
Problem: HR_string split and join
Platform: HackerRank

'''

def split_and_join(line):
    split_line = line.split() # split function will give output string to array
    joint_line = "-".join(split_line) # this will join the array into string again
    return joint_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)