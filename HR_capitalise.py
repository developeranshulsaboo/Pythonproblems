'''
Author: Anshul Saboo
Date: 04/04/2021
Problem: HR_Capitalise
Platform: HackerRank

'''

def solve(s):
    # split the given string to list
    for word in s.split():
        print(s.split())
        # replace each letter by capital 
        s = s.replace(word, word.capitalize())
 
    return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
