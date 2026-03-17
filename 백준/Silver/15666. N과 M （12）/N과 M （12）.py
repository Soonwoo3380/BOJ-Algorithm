import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
result = set()

def lunch(m, chosen, start):
    if len(chosen) == m:
        if tuple(chosen) not in result:
            result.add(tuple(chosen))
            print(*chosen)
        return
    
    for i in range(start, len(num_list)):
        chosen.append(num_list[i])
        lunch(m, chosen, i)
        chosen.pop()

lunch(M, [], 0)