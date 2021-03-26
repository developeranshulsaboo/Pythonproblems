'''
Author: Anshul Saboo
Date: 26/03/2021
Problem: IO_Jaddoo and DNA transcryption
Platform: HackerEarth

'''
#Taking DNA as input in the form of string
dna = str(input())

#Declaring RNA as an empty output string
rna = ""

for x in dna:   #Scaning each character of string
    if (x == "G"):
        rna += "C" #Concatenating the empty string with the replaced character in place of given character
    elif (x == "C"):
        rna += "G"
    elif (x == "T"):
        rna += "A"
    elif (x == "A"):
        rna += "U"
    else:
        rna = "Invalid Input"
        break

print(rna)