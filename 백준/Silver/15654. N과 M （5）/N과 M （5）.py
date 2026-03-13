import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
visited = [False] * len(num_list)

def wow(m, chosen):
    if len(chosen) == m:
        print(*chosen)
        return

    for i in range(len(num_list)):
        if not visited[i]:
            visited[i] = True

            chosen.append(num_list[i])
            wow(m, chosen)
            chosen.pop()

            visited[i] = False

wow(M, [])