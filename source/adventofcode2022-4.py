def createList(rangeset):
    return [item for item in range(int(rangeset[0]), int(rangeset[1])+1)]

contatore = 0
with open("input4.txt", "r") as file:
    data = file.read().splitlines()
    #print(data)
    for half in data:
        elfi = half.split(',')
        lista1 = createList(elfi[0].split('-'))
        lista2 = createList(elfi[1].split('-'))
        if(all(x in lista1 for x in lista2)):
           contatore+= 1
        else:
            if(all(x in lista2 for x in lista1)):
                contatore+= 1
print("parte prima ", contatore)
