import os

max = somma = 0

in_file = open("input1.txt", "r")

for line in in_file:
    if line.strip():   #se la riga non è formata da soli spazi
        somma = somma + int(line)
    else:
        if somma > max:
            max = somma
        somma = 0
in_file.close()
print("max: ", max)
