import re


def main(part1):
    stax,moves = inputAsList()
    for move in moves:
        amount = int(move[0])
        frm = int(move[1])-1
        to = int(move[2])-1
        if(part1):
            for i in range(0,amount):
                crate = stax[frm].pop()
                stax[to].append(crate)
        else:
            crates = stax[frm][-amount:]
            stax[frm] = stax[frm][:-amount]
            stax[to] += (crates)
    result = ""
    for stak in stax:
        result += (stak[len(stak)-1])
    return re.sub(r'\W+', '', result)


def inputAsList():
    f = open('input')
    a,b = f.read().split('\n\n')
    c = inputAsListOfStacks(a)
    d = inputAsListOfMoves(b)
    return c,d

def inputAsListOfStacks(stax):
    splitStax = stax.split('\n')
    num = splitStax[len(splitStax)-1].split('  ')
    stonks = int(num[len(num)-1])                   # figure out the amount of stacks
    staxList = []
    moreStax = []
    for i in range(0,stonks):
        staxList.append([])                         # build a list of stacks
    for j in range(len(splitStax)-2,-1,-1):         # convert the crates to a list
        repair = []
        for h in splitStax[j].split('    '):
            repair += h.split(' ')
        moreStax.append(repair)
    for stak in moreStax:                           # add the crates to the correct stacks in the correct order.
        for s in range(0,stonks):
            if(stak[s] != ''):
                staxList[s].append(stak[s])
    return staxList

def inputAsListOfMoves(moves):
    movelist = []
    moves = moves.split('\n')
    for move in moves:
        movelist.append(re.findall(r'\d+',move))
    return movelist

print(main(True))
print(main(False))
