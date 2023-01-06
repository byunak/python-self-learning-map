### THIS CODE BELOW WILL CREATE A RANDOM PASSWORD FOR THE USER

import random

# There are three lists below to that contains all the possible letters, numbers and symbols
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','-','+','_','=','/','.','?']

# This list below allows us the shuffle the generated password by choosing either a letter, number or a symbol to be used as a password's character
roll = [1,2,3]

# This variable defines how many characters the password will have
charAmount = int(input("How many characters should your password have?"))

# This list stores selected character organization that we randomly got by using the list named roll. There is probably a better way of doing this without messing with two seperate lists to define the order of characters.
selected = []

# This for loop below takes one of the three options that are in the roll[] list and inserts them into the selected[] list for charAmount of times.
for i in range(charAmount):
    choose_next = random.choice(roll)
    selected.append(choose_next)

# This variable below is set to empty for now so that we can fill our characters in with the order that we defined with the selected[] list.
password = ""

# This for loop below fills the password variable with the order that was defined in selected[] list.
for value in selected:
    if value == 1:
        password += random.choice(letters)
    elif value == 2:
        password += random.choice(numbers)
    elif value == 3:
        password += random.choice(symbols)

# This code below prints the random generated password
print(password)