import numpy as np

in_file = open("input8.txt", "r").read().splitlines()
view = 0
mat =np.array([[0] * len(in_file) for i in range(len(in_file[0]))])
matView =np.array([[0] * len(in_file) for i in range(len(in_file[0]))])
for x in range(0,len(in_file)):
    for y in range(0,len(in_file[0])):
        mat[x][y] = in_file[x][y]

for x in range(len(in_file)):
    for y in range(len(in_file[0])):
        view = 0
        for sx in range(y, 0, -1):
            if mat[x][y] > mat[x][sx-1]:
                view += 1
            elif mat[x][y]  <= mat[x][sx-1]:
                view += 1
                break
        matView[x][y] = view
        view = 0

        for dx in range(y+1,len(in_file[0])):
            if mat[x][y] > mat[x][dx]:
                view += 1
            elif mat[x][y]  <= mat[x][dx]:
                view += 1
                break
        matView[x][y] = matView[x][y]*view
        view = 0

        for up in range(x, 0, -1):
            if mat[x][y] > mat[up-1][y]:
                view += 1
            elif mat[x][y]  <= mat[up-1][y]:
                view += 1
                break
        matView[x][y] = matView[x][y]*view
        view = 0

        for down in range(x+1,len(in_file)):
            if mat[x][y] > mat[down][y]:
                view += 1
            elif mat[x][y]  <= mat[down][y]:
                view += 1
                break
        matView[x][y] = matView[x][y]*view

print("Answer2 ", np.max(matView))
