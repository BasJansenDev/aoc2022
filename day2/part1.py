# A X r
# B Y p
# C Z s
wins = {'A' : 'C', 'B' : 'A', 'C' : 'B'}
losses = dict((v,k) for k,v in wins.items())
move_points = {'A' : 1, 'B' : 2, 'C' : 3}
move = {'X' : 'A', 'Y' : 'B', 'Z' : 'C'}

def calculateMatchPoints(a,b):
    if wins[a] == b:
        return 0
    if(a == b):
        return 3
    else:
        return 6

def calculateMatchPoints2(a,b):
    if(b == 'X'):
        return move_points[wins[a]]
    if(b == 'Y'):
        return 3 + move_points[a]
    else:
        return 6 + move_points[losses[a]]

def main(part1):
    lst = inputAsList()
    total = 0
    if(part1):
        for match in lst:
            m = move[match[1]]
            total += move_points[m] + calculateMatchPoints(match[0],m)
    else:
        for match in lst:
            total += calculateMatchPoints2(match[0],match[1])
    return total

def inputAsList():
    f = open('input')
    a = f.read().split('\n')
    c = list()
    for b in a :
        c.append(b.split(' '))
    return c

print(main(True))
print(main(False))