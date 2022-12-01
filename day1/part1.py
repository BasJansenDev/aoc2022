def main(part1):
    list = inputAsList()
    newList = []
    for cals in list :
        newList.append(sum(cals))
    newList.sort()
    newList.reverse()
    if(part1):
        return newList[0]
    else:
        return newList[0] + newList[1] + newList[2]


def inputAsList():
    f = open('input')
    a = f.read().split('\n\n')
    c = list()
    for b in a :
        c.append(map(int,(b.split('\n'))))
    return c

print(main(True))
print(main(False))