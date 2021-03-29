'''
Author: Anshul Saboo
Date: 29/03/2021
Problem: HR_Nested List
Platform: HackerRank

'''

#Declaraing dictionary which is empty
dictionary = {}

# Taking input of name and grade using for loop
for _ in range(int(input())):
    name = input()
    grade = float(input())
    dictionary[name] = grade #Assigning name as key variable and grade as value

dictionary_values = dictionary.values() #getting the values from dictionary
second_lowest_grade = sorted(list(set(dictionary_values)))[1] #Find the second lowest number in dictionary_values and storing in list form

second_lowest_list = []
for key, value in dictionary.items():
    if value == second_lowest_grade:
        second_lowest_list.append(key)
second_lowest_list.sort()
for name in second_lowest_list:
    print(name)
