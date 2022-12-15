import re
from z3 import If, Int, Solver

with open("input15.txt", "r") as file:
    rows= file.read().strip().split("\n")

data = [list(map(int, re.findall("-?\d+", ch))) for ch in rows]

manhattan = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

# Part 2: use z3 fast!!!
def z3abs(x):
    return If(x >= 0, x, -x)

s = Solver()
x = Int("x")
y = Int("y")
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)
for dato in data:
    distance = manhattan(dato[0], dato[1], dato[2], dato[3])
    s.add(z3abs(x - dato[0]) + z3abs(y - dato[1]) > distance)

s.check()
model = s.model()
print("answer2 ", model[x].as_long() * 4000000 + model[y].as_long())
