import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())

with open("input3Test.txt", "r") as file:
    data = file.read().splitlines()
    #print(data)
    somma = 0
    conta = 0
    riga = ['','','']
    for half in data:
        if conta == 3:
            conta = 1
            ch = ''.join(set(riga[0])  & set(riga[1]) & set(riga[2]))
            if ch >= "a":
                priority = ord(ch)-96
                print("priorità ", priority)
            else: 
                priority = ord(ch)-38
                print("priorità ", priority)
            somma = somma + priority
            riga = [half,'','']
        else:
            riga[conta]= half
            conta +=1
    ch = ''.join(set(riga[0])  & set(riga[1]) & set(riga[2]))
    if ch >= "a":
        priority = ord(ch)-96
        print("priorità ", priority)
    else: 
        priority = ord(ch)-38
        print("priorità ", priority)
    somma = somma + priority
print("totale  ", somma)
