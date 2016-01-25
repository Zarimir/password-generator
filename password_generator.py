from random import randint
#import os

#DEFINITIONS...
# Password to clipboard
#def addToClipBoard(text):
#    command = 'echo ' + text.strip() + '| clip'
#    os.system(command)

# Random list values
def value(my_list):
    list_value = my_list[randint(0, len(my_list) - 1)]
    list_value = str(list_value)
    return list_value

# Raw_input + convert to number + number > 4
def pass_length():
    try:
        password_length = int(input("Please choose password length larger than 4:\n>> "))
        while password_length < 5:
            password_length = int(input("Please choose password length larger than 4:\n>> "))
        return password_length
    except ValueError:
        print ("Invalid value, please restart the program and use a number")
        input("Pess ENTER to exit and restart the program")
        exit()

# Upper_case_position
def uppercase():
    upper_case_position = randint(0, password_length - 1)
    while upper_case_position == lower_case_position:
        upper_case_position = randint(0, password_length - 1)
    return upper_case_position

# Number_position
def number():
    numbers_position = randint(0, password_length -1)
    while numbers_position == lower_case_position or numbers_position == upper_case_position:
        numbers_position = randint(0, password_length -1)
    return numbers_position

# Symbol_position
def symbol():
    symbols_position = randint(0, password_length -1)
    while symbols_position == lower_case_position or symbols_position == upper_case_position or symbols_position == numbers_position:
        symbols_position = randint(0, password_length -1)
    return symbols_position

# Final password
def password_fix(position, value):
    password[position] = value

# END of definitions;
# CODE...

# Lists
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '*', '(',')', '_', '-']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
password_symbols = lower_case + upper_case + symbols + numbers

# Random value per list
lower_case_value = value(lower_case)
upper_case_value = value(upper_case)
symbols_value = value(symbols)
numbers_value = value(numbers)

# Raw_input
password_length = pass_length()

# Test
'''
print ("password length")
print (password_length)
'''

# Password full random
password = []
for i in range(password_length):
    # Password.append(i)
    pass_symbol = str(password_symbols[randint(0, len(password_symbols) - 1)])
    password.append(pass_symbol)

# Test
'''
print ("random password")
print (password)
'''

# Positions
lower_case_position = randint(0, password_length - 1)
upper_case_position = uppercase()
numbers_position = number()
symbols_position = symbol()

# Test
'''
print ("lower_case is")
print (lower_case_position + 1)
print ("upper_case is")
print (upper_case_position + 1)
print ("number is")
print (numbers_position + 1)
print ("symbol is")
print (symbols_position + 1)
'''

# Password_output
password_fix(lower_case_position, lower_case_value)
password_fix(upper_case_position, upper_case_value)
password_fix(numbers_position, numbers_value)
password_fix(symbols_position, symbols_value)
pass_export = "".join(password)
# Test
print ("password:")
'''
print ("")
print (password)
print ("")
print ("or")
print ("")
'''
print (pass_export)
#print ("")
#print ("The password is on your clipboard, use CTRL + V to paste it anywhere you want.")
#addToClipBoard(pass_export)
input()
