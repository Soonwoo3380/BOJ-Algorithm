import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
visited = [False] * N
compare = set()

def evening_2(m, chosen):
    if len(chosen) == m:
        if tuple(chosen) not in compare:
            compare.add(tuple(chosen))
            print(*chosen)
            return
    
    for i in range(len(num_list)):
        if not visited[i]:
            visited[i] = True
            chosen.append(num_list[i])
            evening_2(m, chosen)
            chosen.pop()
            visited[i] = False

evening_2(M, [])