values = {}
opers = {}
finish = False

def findit(name):
    for oper in opers:
        finish = False
        tot = 0
        left, op, right = opers[oper]
        if isinstance(left, int) and isinstance(right, int):
            finish = True
            if op == "+":
                tot = left + right
            elif op == '-':
                tot = left - right
            elif op == "*":
                tot = left * right
            elif op == "/":
                tot = int(left / right)
            del opers[oper] 
            break
        else:
            if not isinstance(left, int) and name in left:
                opers[oper][0]= values[name]
            elif not isinstance(right, int) and name in right:
                opers[oper][2]=values[name]
    return(oper, tot, finish )

lines = open('input21Test.txt').read().splitlines()
for line in lines:
    monkey, *oper = line.split()
    monkey = monkey.replace(':', '').strip()
    if len(oper) == 1:
        values[monkey] = int(oper[0])
    else:
        opers[monkey] = oper

while True:
    for value in values:
        if finish:
            values[esito] = tot
            finish = False
            break
        esito, tot, finish = findit(value)
    if esito== "root" and tot > 0:
        break
print("answer1 ", tot)
