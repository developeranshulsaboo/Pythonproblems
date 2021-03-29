dictionary = {}

for _ in range(int(input())):
    name = input()
    grade = float(input())
    dictionary[name] = grade

dictionary_values = dictionary.values()
second_lowest_grade = sorted(list(set(dictionary_values)))[1]

second_lowest_list = []
for key, value in dictionary.items():
    if value == second_lowest_grade:
        second_lowest_list.append(key)
second_lowest_list.sort()
for name in second_lowest_list:
    print(name)