import re

with open("input15.txt", "r") as file:
    rows= file.read().strip().split("\n")

data = [list(map(int, re.findall("-?\d+", ch))) for ch in rows]

manhattan = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

counter = 0
y = 2000000

#part 1: bruteforce slow, please wait
for x in range(-6000000, 6000000):
    ispossible = True
    for sx,sy,bx,by in data:
        if (x,y) == (bx,by):
            ispossible = True
            break
        if manhattan(sx,sy,x,y) <= manhattan(sx,sy,bx,by):
            ispossible = False
            break
    if not ispossible:
        counter += 1
print("answer1 ", counter)
