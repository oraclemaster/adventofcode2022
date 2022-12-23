r = 0
d = [ ( 0, -1 ), ( 0, 1 ), ( -1, 0 ), ( 1, 0 ) ]

with open('input23.txt') as f:
    pos = { ( x, y )
        for y, r in enumerate(f.readlines())
        for x, c in enumerate( r.strip( '\n' ) )
            if c == '#' }

while True:
    r +=1
    proposed = {}
    for x,y in pos:
        moves = [(x-1, y-1), (x,y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1,y+1), (x-1, y)]
        for mx,my in moves:
            if (mx, my) in pos:
                for dx, dy in d:
                    pos_to_check = []
                    possible = True
                    for mx, my in moves:
                        if (dx == 0 and my - y == dy) or (dy == 0 and mx -x == dx):
                            if (mx, my) in pos:
                                possible = False
                                break
                    if possible:
                        if (x+dx, y+dy) in proposed:
                            proposed[(x+dx, y+dy)] = None
                        else:
                            proposed[(x+dx, y+dy)] = (x,y)
                        break
                break

    if not proposed:
        break
    for (mx, my), find in proposed.items():
        if find:
            pos.remove(find)
            pos.add((mx, my))
    
    setx = [x for x,y in pos]
    sety = [y for x,y in pos]
    minx = min(x, *setx)
    maxx = max(x, *setx)
    miny = min(y, *sety)
    maxy = max(y, *sety)
    d = d[1:] + d[:1]

    if r == 10:
        print('answer1', (maxx - minx + 1) * (maxy - miny + 1) - len(pos))
print('answer2', r)
