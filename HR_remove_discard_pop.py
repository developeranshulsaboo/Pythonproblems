'''
Author: Anshul Saboo
Date: 06/04/2021
Problem: HR_string split and join
Platform: HackerRank

'''
# taking the size of set
n = int(input())

# Declaraing empty set
s = set(map(int, input().split()))

# Taking the number of commands to run
N = int(input())

# remove function generates error if the element is not present while discard does not generates error
# running for loop for N time
for i in range(N):
    choice = input().split()
    if(choice[0] == 'pop'):
        s.pop()
    elif(choice[0] == 'remove'):
        s.remove(int(choice[1]))
    elif(choice[0] == 'discard'):
        s.discard(int(choice[1]))

print(sum(s)) 