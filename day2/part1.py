# A X r
# B Y p
# C Z s
draws = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}
wins = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}
pts = {'X' : 1, 'Y' : 2, 'Z' : 3}
pt = {'X' : 0, 'Y' : 3, 'Z' : 6}
move = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}

def winCalc(a,b):
    if wins[a] == b:
        return 0
    if(draws[a] == b):
        return 3
    else:
        return 6

def winCalc2(a,b):
    if(b == 'X'):
        return wins[a]
    if(b == 'Y'):
        return draws[a]
    else:
        return move[[k for k, v in wins.items() if v == move[a]][0]]

def main():
    lst = inputAsList()
    total = 0
    for match in lst:
        total += pts[match[1]] + winCalc(match[0],match[1])
    return total

def main2():
    lst = inputAsList()
    total = 0
    for match in lst:
        total += pt[match[1]] + pts[winCalc2(match[0],match[1])]
    return total

def inputAsList():
    f = open('input')
    a = f.read().split('\n')
    c = list()
    for b in a :
        c.append(b.split(' '))
    return c

print(main())
print(main2())