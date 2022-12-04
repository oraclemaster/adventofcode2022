import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())

with open("input3Test.txt", "r") as file:
    data = file.read().splitlines()
    somma = 0
    for half in data:
        res_first, res_second = half[:len(half)//2], half[len(half)//2:]
        #find common elements present in 2 strings
        ch = ''.join(set(res_first).intersection(res_second))
        if ch >= "a":
            priority = ord(ch)-96
        else: 
            priority = ord(ch)-38
        somma = somma + priority
print("totale  ", somma)
