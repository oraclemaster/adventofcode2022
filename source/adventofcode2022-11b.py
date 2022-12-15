divisor = 1
monkeys = []

class Monkey:
    def __init__(self, m):
        for l in line.splitlines():
            r=l.strip().split()
            if r[0]== "Starting":
                self.items = [int(r[x].replace(",","")) for x in range(2,len(r))]
            elif r[0] == "Operation:":
                self.operation = (r[4],r[5])
            elif r[0] == "Test:":
                self.test = int(r[3])
            elif r[0] == "If":
                if r[1] == "true:":
                    self.is_true = int(r[5])
                else:
                    self.is_false = int(r[5])

        self.inspected= 0

    def roundb(self):
        result = []
        for i in self.items:
            self.inspected+= 1
            livello= eval(
                "i" + self.operation[0] + self.operation[1].replace("old", "i"))
            result.append((self.is_true if livello %
                       self.test == 0 else self.is_false, livello))
        self.items = []

        return result

for line in open("input11.txt").read().split("\n\n"):
    monkeys.append(Monkey(line))

for lines in monkeys:
    divisor = divisor * lines.test

for round in range(10000):
    for line in range(len(monkeys)):
        tmp = monkeys[line].roundb()
        for i in tmp:
            monkeys[i[0]].items.append(i[1] % divisor)
monkeys.sort(key=lambda x: x.inspected, reverse=True)

print("answer2 ", monkeys[0].inspected * monkeys[1].inspected)
