import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [num for num in range(1, N+1)]
visited = [False] * N
def comb(m, chosen, start):
    if len(chosen) == m:
        print(*chosen)
        return
    
    for i in range(start, len(numbers)):
        if not visited[i]:
            visited[i] = True
            chosen.append(numbers[i])
            comb(m, chosen, i)
            chosen.pop()
            visited[i] = False

comb(M, [], 0) 