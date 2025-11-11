# r - read
# a - append
# w - write
# x - create


f = open("names.txt","r")
# print(f.read())

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()