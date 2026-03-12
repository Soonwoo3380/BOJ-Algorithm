import sys
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

result = []

found = False

def combi(start, chosen):
    global found
    if found:
        return

    if len(chosen) == 7:
        if sum(chosen) == 100:
            for num in chosen:
                print(num)
            found = True
        return
    
    for i in range(start, 9):
        chosen.append(dwarfs[i])
        combi(i+1, chosen)
        chosen.pop()

combi(0, [])