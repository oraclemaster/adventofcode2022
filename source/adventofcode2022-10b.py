in_file= open("input10.txt").read().strip().split("\n") # prod

regx = 1
value = cycle = row = 0
half = False
crt= ''

while row < len(in_file):
    cycle += 1

    if ((cycle-1) % 40) in [regx-1, regx, regx+1]:
        crt+= '[]'
    else:
        crt += '  '
    if (cycle % 40) == 0:
        crt += '\n'
    
    line = in_file[row]
    if line[0] == "n":
        row +=1 
    else:
        command, value = line.split()
        if half == True:
            regx = regx + int(value)
            half = False
            row+= 1
        else:
            half = True

print(crt)
