in_file= open("input10.txt").read().strip().split("\n") # prod

regx = 1
value = cycle = strenght = row = 0
half = False

while row< len(in_file):
    cycle += 1
    if cycle ==20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle ==220:
        strenght = strenght + (cycle*regx)
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

print("answer1 ", strenght)
