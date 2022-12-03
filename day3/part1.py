def numMap(asd):
    a = ord(asd.pop()) - 96
    if(a < 0):
        return a + 58
    else:
        return a

def main(part1):
    lst = inputAsList()
    total = 0
    if(part1):
        for items in lst:
            comp1, comp2 = set(items[:len(items)//2]), set((items[len(items)//2:]))
            total += numMap(comp1 & comp2)
    else:
        while lst != []:
            comp1, comp2, comp3 = lst[:3]
            total += numMap(set(comp1) & set(comp2) & set(comp3))
            lst = lst[3:]
    return total

def inputAsList():
    f = open('input')
    a = f.read().split('\n')
    return a

print(main(True))
print(main(False))