def main(part1):
    lst = inputAsList()
    total = 0
    for pair in lst:
        r1 = pair[0].split('-')
        r2 = pair[1].split('-')
        r1 = set(range(int(r1[0]),int(r1[1])+1))
        r2 = set(range(int(r2[0]),int(r2[1])+1))
        total += (part1 and (r1 <= r2 or r2 <= r1)) or (not part1 and len(r1 & r2) > 0)
    return total

def inputAsList():
    f = open('input')
    a = f.read().split('\n')
    b = list(map(lambda x: x.split(','),a))
    return b

print(main(True))
print(main(False))