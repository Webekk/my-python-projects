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