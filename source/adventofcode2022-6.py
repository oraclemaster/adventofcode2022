import os

def removeDuplicate(str):
    if len(str) == 4:
        if len("".join(set(str))) == 4:
            return True

in_file = open("input6.txt", "r")

for line in in_file:
    for i in range(len(line)):
        if removeDuplicate(line[i:i+4]):
            break
    print("Result1: ",i+4)

in_file.close()
