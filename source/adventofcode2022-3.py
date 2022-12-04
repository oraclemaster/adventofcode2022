import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())

with open("input3Test.txt", "r") as file:
    data = file.read().splitlines()
    somma = 0
    for half in data:
        res_first, res_second = half[:len(half)//2], half[len(half)//2:]
        print("First part: ", res_first, " second part: ", res_second)
        #find common elements present in 2 strings
        ch = ''.join(set(res_first).intersection(res_second))
        print("carattere comune ", ch)
        if ch >= "a":
            priority = ord(ch)-96
            print("priorità ", priority)
        else: 
            priority = ord(ch)-38
            print("priorità ", priority)
        somma = somma + priority
print("totale  ", somma)
