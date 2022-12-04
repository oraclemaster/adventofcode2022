import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())

numrec = 0
max = 0
somma = 0

in_file = open("input1.txt", "r")

for line in in_file:
    
    numrec+=1
    if line.strip():   #se la riga non è formata da soli spazi
        somma = somma + int(line)
    else:
        print("totale parziale: ", somma)
        if somma > max:
            max = somma
        somma = 0
in_file.close()
print("record letti ", numrec, " max: ", max)
