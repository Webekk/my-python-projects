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
