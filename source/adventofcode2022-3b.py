with open("input3.txt", "r") as file:
    data = file.read().splitlines()
    #print(data)
    somma = conta = 0
    riga = ['','','']
    for half in data:
        if conta == 3:
            conta = 1
            ch = ''.join(set(riga[0])  & set(riga[1]) & set(riga[2]))
            if ch >= "a":
                priority = ord(ch)-96
            else: 
                priority = ord(ch)-38
            somma = somma + priority
            riga = [half,'','']
        else:
            riga[conta]= half
            conta +=1
    ch = ''.join(set(riga[0])  & set(riga[1]) & set(riga[2]))
    if ch >= "a":
        priority = ord(ch)-96
    else: 
        priority = ord(ch)-38
    somma = somma + priority
print("totale  ", somma)
