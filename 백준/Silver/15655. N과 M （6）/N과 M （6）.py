import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split()))) # N = len(num_list)
visited = [False] * N

def helloworld(m, start, chosen):
    if len(chosen) == m:
        print(*chosen)
        return

    for i in range(start, len(num_list)):

        if not visited[i]:
            visited[i] = True
            chosen.append(num_list[i])
            helloworld(m, i+1, chosen)
            chosen.pop()
            visited[i] = False
       
helloworld(M, 0, [])