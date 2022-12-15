import functools

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

packets, packets_divider = [], [[[2]], [[6]]]
for p in open('input13.txt').read().split('\n\n'):
    left, right = map(eval, p.split('\n'))
    packets.append((left, right))
    packets_divider += [left, right]

packets_sorted = sorted(packets_divider, key=functools.cmp_to_key(compare))
print("answer2 ", (1 + packets_sorted.index([[2]])) * (1 + packets_sorted.index([[6]])))
