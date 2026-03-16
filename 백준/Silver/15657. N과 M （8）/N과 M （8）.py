import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())), reverse=False)

def evening(m, start, chosen):
    if len(chosen) == m:
        print(*chosen)
        return
    
    for i in range(start, len(num_list)):
        chosen.append(num_list[i])
        evening(m, i, chosen)
        chosen.pop()

evening(M, 0, [])