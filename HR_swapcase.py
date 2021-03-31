'''
Author: Anshul Saboo
Date: 31/03/2021
Problem: HR_Swapcase
Platform: HackerRank

'''
#We have to create a function to solve this function
#We will be using inbuilt swapcase() function in between user defined swap_case
#The swapcase function converts the lowercase letter to uppercase and vice versa in string one by one
def swap_case(s):
    return s.swapcase()


s = str(input())
result = swap_case(s)
print(result)