# 2. Add Key to Dictionary
sampleDict = {
    "first" : 130,
    "second" : 2,
    "third" : 24,
    "fourth" : 0,

}

print(sampleDict)
# sampleDict[3] = 30

print(sampleDict)

#  Sort Dictionary by Value

val_based = {k: v for k, v in sorted(sampleDict.items(), key=lambda item: item[1])}
val_basedReversed = {k: v for k, v in sorted(sampleDict.items(), key = lambda item: item[1],reverse = True)}

print(val_based)
print(f"Descending order {val_basedReversed}")
print(f"Ascending order {val_based}")

# Concatenate Dictionaries

dic1={1:100, 2:20, 3: 10, 4: 20, 5 : 10, 6 : 20, 7: 10, 8 : 20, 9: 10, 10: 10}
dic2={3:30, 4:40}
dic3={5:50,6:60}


dicConcat = dic1 | dic2 | dic3 # This creates a new dictionary without modifying the old ones Python 3.9+
dicConcat2 = {**dic1, **dic2, **dic3} # Dictionary unpacking
# dic1.update(dic2) # Changing a dictionary by using function update()
# dic1.update(dic3)
print(dic1)
# print(dicConcat)


# Check if the certain key exist in the dictionary (using a for loop)

for k, v in dic1.items():
    if k == 10:
        print(f"The key 10 exists in the dictionary")


# Check if the certain key exist in the dictionary (using a function)

def checkNumberInDict(number):
    # Number as a key and dic1 is my dictionary that was created above
    if number in dic1:
        print(f"The key {number} is in the dictionary")
    else:
        print(f"The key {number} is not in the dictionary")

checkNumberInDict(9)

# 5. Iterate Over Dictionary Using For Loops

for k, v in dic1.items():  # k stands for key and v stands for value
    print(f"The key {k} : value {v}")

#  Generate Dictionary of Numbers and Their Squares

# (My solution) Creating the dict outside function and using update to manipulate it
def create_squareDictionary(number,square_dictionary):
    for i in range(1,number + 1):
        square_dictionary.update({i : i * i})

    return f"This is my take on a solution: {square_dictionary}"

"""The solutions are nearly the same but this one is less elegant
   I came up with idea for it and i feel super proud about my progress
"""

testDictionary = {}

result_of_dictionary_squares = create_squareDictionary(20,testDictionary)
print(result_of_dictionary_squares)

print("--------------------------------------------------------------")
# Optimizing the solution, using one parameter and making the dictionarie inside the function

def optimized_squareDict(number):
    dictionary = {}
    for i in range(1, number + 1):
        dictionary[i] = i * i
    return f"This is an optimized solution: {dictionary}"
square_dictionary = optimized_squareDict(20)
print(square_dictionary)

# I like this solution a lot more, i'm not using an external dict but i'm creating a new one inside the method
# This allows me to manipulate it better and prompt the solution for given number a lot quicker without need of
# Creating a new dictionaries outside the body of a function

# Dictionary with Keys 1 to 15 and Their Squares

def one_to_fifteen():
    dictionary = {}
    for i in range(1, 16): # including a range from 1 to 15
        dictionary[i] = i ** 2

    return dictionary

result = one_to_fifteen() # Need to put this in to variable so we can print it out as we want to
print(result)


