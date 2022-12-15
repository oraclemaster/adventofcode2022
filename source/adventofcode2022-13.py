def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 0 if left == right else (-1 if left < right else 1)
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    elif left and right:
        temp = compare(left[0], right[0])
        return temp if temp else compare(left[1:], right[1:])
    return 1 if left else (-1 if right else 0)

packets = []
for p in open('input13.txt').read().split('\n\n'):
    left, right = map(eval, p.split('\n'))
    packets.append((left, right))

tot = 0
minore = True
for indice, packet in enumerate(packets):
    if compare(packet[0], packet[1]) == -1:
        tot= tot + indice + 1
print ("answer1 ", tot)
