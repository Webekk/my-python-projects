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

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}


dicConcat = dic1 | dic2 | dic3 # This creates a new dictionary without modifying the old ones Python 3.9+
dicConcat2 = {**dic1, **dic2, **dic3} # Dictionary unpacking
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
# print(dicConcat)