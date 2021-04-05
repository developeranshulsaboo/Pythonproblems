'''
Author: Anshul Saboo
Date: 05/04/2021
Problem: HR_Introduction to sets
Platform: HackerRank

'''
# Problem does nor allow you to directly take input in the form of set so we are converting it in function
# Set gives proper output rather than list because we can add int and float in set but not together in list

def average(array):
    array = set(array)
    result = sum(array) / len(array)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)