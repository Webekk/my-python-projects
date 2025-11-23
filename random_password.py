# Here is the link for the password generator
# https://www.geeksforgeeks.org/python/create-a-random-password-generator-using-python/
import string
import random

while True:
    try:
        length = int(input("Enter password length: "))
        if length > 0:
         break
        else:
            print("Password length must be greater than 0")
    except ValueError:
        print("Password length must be greater than 0")

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
characterList = ""

# Getting character set for password
while True:
    choice = int(input("Pick a number: "))
    if choice == 1:

        # Adding letters to possible characters
        characterList += string.ascii_letters
        print(characterList)
    elif choice == 2:

        # Adding digits to possible characters
        characterList += string.digits
        print(characterList)
    elif choice == 3:

        # Adding special characters to possible characters
        characterList += string.punctuation
        print(characterList)
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    randomChar = random.choice(characterList)

    password.append(randomChar)
print("The random password is " + "".join(password))
type_of_password = input("Enter the password destination of use: ")

with open("passwords.txt", "a") as file:
    file.write(type_of_password + ": ")
    file.write("".join(password))
    file.write("\n")

with open("passwords.txt", "r") as file:
    print("Here are all the passwords: ")
    print(file.read())

