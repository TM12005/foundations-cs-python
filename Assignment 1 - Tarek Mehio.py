# num1 = input("Enter the first number:")
# num2 = input("Enter the second number:")
import re

names = ["Maria", "Hala", "Hady", "Ehsan", "Joe", "Zoe"]
while True:   
   letter = input("Enter a letter")
   for i in range(len(names)):
       if names[i].__contains__(letter.lower(), letter.upper()):
           print(names[i])
          