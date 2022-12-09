position = ["0-0"]
in_file = open("input9.txt", "r")

ver = hor = vert = hort = 0
for data in in_file:
    dir, dist = data.split()
    for a in range(int(dist)):
        if dir == "R":
            hor +=1
        elif dir == "L":
            hor -= 1
        elif dir == "U":
            ver +=1
        else:
            ver -= 1
        if abs(hor - hort) > 1 or abs(ver-vert) > 1:
            if hor > hort:
                hort +=1
            elif hor < hort:
                hort -=1
            if ver > vert:
                vert +=1
            elif ver < vert:
                vert -=1
        posStr = str(hort)+"-"+ str(vert)
        if posStr not in position:
            position.append(posStr)

print("answer1 ", len(position))
