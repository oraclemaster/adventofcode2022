import numpy as np

in_file = open("input8.txt", "r").read().splitlines()
righe= len(in_file)-2
somma= len(in_file[0])*2+ len(in_file)*2 -4
mat =np.array([[0] * len(in_file) for i in range(len(in_file[0]))])
for x in range(0,len(in_file)):
    for y in range(0,len(in_file[0])):
        mat[x][y] = in_file[x][y]

for x in range(1,len(in_file)-1):
    for y in range(1,len(in_file[0])-1):
        if mat[x][y] > mat[x, :y].max() or mat[x][y] > mat[x, y+1:].max() or mat[x][y] > mat[:x, y].max() or mat[x][y] > mat[x+1:, y].max():
            somma +=1
print("Answer1 ", somma)
