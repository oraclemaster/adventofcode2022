from itertools import zip_longest

rows = open('input5.txt').read().split('\n\n')

stack = rows[0].split('\n')
del stack[-1]
stack1 = transposed = reverselist = []
for x in stack:
    stack1.append([x[i:i + 4].translate({ord(i): None for i in ' []'}) for i in range(0, len(x), 4)])

tranposed_tuples = zip_longest(*stack1, fillvalue=None)
transposed_list = list(tranposed_tuples)
transposed = [list(sublist) for sublist in transposed_list]
transposed = [list(filter(None, lst)) for lst in transposed]

command = [[int(y) for y in x.split() if y.isdigit()] for x in rows[1].split('\n') if x]
command = [(a, b-1, c-1) for a,b,c in command]

for a,b,c in command:
    transposed[c] =  transposed[b][:a] + transposed[c]
    transposed[b] = transposed[b][a:]

print("".join(x[0] for x in transposed))
