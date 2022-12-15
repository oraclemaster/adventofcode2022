from itertools import tee 

position = ["0-0"]
in_file = open("input9.txt", "r")

ver = hor = vert = hort = 0
for data in in_file:
    dir, dist = data.split()
    if dir == "R":
        hor = hor + int(dist)
    elif dir == "L":
        hor = hor - int(dist)
    elif dir == "U":
        ver = ver + int(dist)
    else:
        ver == ver - int(dist)
    print("posizione ", ver,hor)
    if abs(ver - vert) > 1 or abs(hor-hort) > 1:
        if hor > hort:
            hort = hort + hor
        else:
            hort = hort - hor
        if ver > vert:
            vert = vert + ver
        else:
            vert = vert-ver
    print("pos Tabil ", vert,hort)
    posStr = str(vert)+"-"+ str(hort)
    if posStr not in position:
       position.append(posStr)
    print (position)

def follow(head):
    x = y = 0 
    for hx, hy in head:
        if abs(hx - x) > 1 or abs(hy - y) > 1:
            y += (hy > y) - (hy < y)
            x += (hx > x) - (hx < x)
        yield x, y

second, tenth = tee(follow(move()))
for _ in range(8):
    tenth = follow(tenth)
print("answer1 ", len(position))
print("answer2 ", len(set(tenth)))
