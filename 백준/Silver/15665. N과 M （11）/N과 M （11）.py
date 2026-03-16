import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
compare = set()

def evening_4(m, chosen):
    if len(chosen) == m:
        if tuple(chosen) not in compare:
            compare.add(tuple(chosen))
            print(*chosen)
        return
    
    for i in range(0, len(num_list)):
        chosen.append(num_list[i])
        evening_4(m, chosen)
        chosen.pop()

evening_4(M, [])