def removeDuplicate(str, maxlen):
    if len(str) == maxlen: 
        if len("".join(set(str))) == maxlen: return True

in_file = open("input6.txt", "r")

for line in in_file:
    for i in range(len(line)):
        if removeDuplicate(line[i:i+4],4):
            break
    print("Result1: ",i+4)

for i in range(len(line)):
    if removeDuplicate(line[i:i+14],14):
        break
print("Result2: ",i+14)

in_file.close()
