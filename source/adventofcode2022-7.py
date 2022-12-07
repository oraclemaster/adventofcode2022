in_file = open("input7.txt", "r")

dir =[]
dim = []
for line in in_file:
    cmd = line.split()
    if cmd[0] == "$":
        if cmd[1] == "cd" and cmd[2] == "..":
            dim.append(dir.pop(-1))
            if dir:
                dir[-1] += dim[-1]
        elif cmd[1] == "cd":
            dir.append(0)
    else:
        if cmd [0] != "dir":
            dir[-1] += int(cmd[0])

conta =0
while dir:
    dim.append(dir.pop(-1))
    if dir:
        dir[-1] += dim[-1]

print("Answer1 ", sum(x for x in dim if x <= 100000))
print("Answer2 ", min(y for y in dim if y >= (max(dim) - 40000000)))
