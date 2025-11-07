import collections

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

# 8. Merge Two Python Dictionaries

merged_dictionaries = result | dic1 # That's a quick way to do it but lacks modularity in my opinion
# Keys from 1 to 10 share the same key
#so they are overwritten by dic1 dictionary
print(f"These are the 2 merged dictioanries {merged_dictionaries}")

# for x in merged_dictionaries: # printing all the keys
#     print(f"Key: {x}", end = " ")
#     print(f"Value: {merged_dictionaries[x]}")
# That is actually good but i can do that with one simple for loop


for k, v in merged_dictionaries.items():
    print(f"Key: {k}, Value: {v}")


sum_of_dictionarie = sum(merged_dictionaries.values()) # Everytime I want to sum some values i can use sum() function
print("First solution: ",sum_of_dictionarie)

values = 0
values2 = 0
sample_dictionary = {
    "first" : 130,
    "second" : 2,
    "third" : 24
}
for v in sample_dictionary.values():

      values += v
print(f"Iterative way of summing the values from the dictionary: {values}")


for v in merged_dictionaries.values():
    values2 += v

print(values2)

# Yeah, I had problems with this one
    # thought there's a problem with merged dictionaries
    # but that was only a problem with my logic

del merged_dictionaries[2]
print(merged_dictionaries)

multiply_score = 1 # Made a wrong base case on this one, it's logical that if you multiply by 0 it's always gonna be a zero so it's better to leave 1 to let it manage the calculations
for v in sampleDict.values():
    multiply_score *= v

print(multiply_score)

list1 = [10,2,1,2,3,4,5]
list2 = ["Hank", "Walter", "Jesse"]

breaking_bad_dictionary = dict(zip(list1, list2))



print(f"Before sorting by key: {breaking_bad_dictionary}")
# Sorting dictionary by key

od = collections.OrderedDict(sorted(breaking_bad_dictionary.items()))

# And now my sorted by key dict is inside the "od" variable and now I can access the sorted key by simply calling the variable
# like here
print(f"After sorting by key: {od}")

for k, v in od.items():
    print(f"Key: {k}, Value: {v}")

#Get minimum and maximum values from a dictionary

print(max(breaking_bad_dictionary.values()))
print(min(breaking_bad_dictionary.values()))

# 16. Get Dictionary from an Object's Fields

class DictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "yellow"
        self.z=  "blue"

    def nothing(self):
        pass

dictObj = DictObj()
print(dictObj.__dict__)