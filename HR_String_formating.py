'''
Author: Anshul Saboo
Date: 03/04/2021
Problem: HR_String Formating
Platform: HackerRank

'''

def print_formatted(number):
    # Declaraing Empty Strings
    decimal_numbers = [] 
    octal_numbers = []
    hexadecimal_numbers = []
    binary_numbers = []

    # for loop for append decimal numbers in the 1'st empty list
    for i in range(number):
        i += 1
        decimal_numbers.append(i)
    
    # for loop for append & finding octal numbers in 2'nd list
    for j in range(number):
        j += 1
        octal_numbers.append(oct(j).replace("0o", ""))
    
    # for loop for append & finding hexadecimal numbers in 2'nd list
    for k in range(number):
        k += 1
        hexadecimal_numbers.append(hex(k).replace("0x", "").upper())

    # for loop for append & finding binary numbers in 2'nd list
    for l in range(number):
        l += 1
        binary_numbers.append(bin(l).replace('0b', ''))

    # converting list to string one by one and printing
    for m in range(number):
        print(str(decimal_numbers[m])+"   "+str(octal_numbers[m])+"   "+str(hexadecimal_numbers[m])+ "   "+str(binary_numbers[m]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    