def createList(rangeset):
    return [item for item in range(int(rangeset[0]), int(rangeset[1])+1)]

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

answer1 = answer2 = 0
with open("input4.txt", "r") as file:
    data = file.read().splitlines()
    for half in data:
        elfi = half.split(',')
        list1 = createList(elfi[0].split('-'))
        list2 = createList(elfi[1].split('-'))
        if(all(x in list1 for x in list2)):
           answer1+= 1
        else:
            if(all(x in list2 for x in list1)):
                answer1+= 1
        if len(intersection(list1, list2)) > 0:
            answer2 +=1
print("Part One: ", answer1)
print("Part Two: ", answer2)
