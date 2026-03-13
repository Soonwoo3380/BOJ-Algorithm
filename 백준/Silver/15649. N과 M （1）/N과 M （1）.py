N, M = map(int, input().split())


num_list = [i for i in range(1, N+1)]
visited = [False] * (N+1)

def comb(m, chosen):
    if len(chosen) == m:
        print(*chosen)
        return

    for k in range(len(num_list)):
        if not visited[k]:
            visited[k] = True
            chosen.append(num_list[k])
            comb(m, chosen)
            chosen.pop()
            visited[k] = False

comb(M, [])