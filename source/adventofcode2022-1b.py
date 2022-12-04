import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())
in_file = open("input1.txt", "r")

max = [0,0,0]
totale = somma = 0

for line in in_file:
    
    numrec+=1
    if line.strip():   #se la riga non è formata da soli spazi
        somma = somma + int(line)
    else:
        if somma > min(max):
            max[0] = somma
            max.sort()
        somma = 0
    
if somma > min(max):
    max[0] = somma
in_file.close()

for num in max:
    totale = totale + num
