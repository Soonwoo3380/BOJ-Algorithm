import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
visited = [False] * N
compare = set()

def evening_3(m, chosen, start):
    if len(chosen) == m:
        if tuple(chosen) not in compare:
            compare.add(tuple(chosen))
            print(*chosen)
            return
    
    for i in range(start, len(num_list)):
        if not visited[i]:
            visited[i] = True
            chosen.append(num_list[i])
            evening_3(m, chosen, i+1)
            chosen.pop()
            visited[i] = False

evening_3(M, [], 0)