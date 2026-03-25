import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = []
result.append((N, 0))
visited = [False] * (100000+1)

idx = 0

while idx < len(result):
    pos, time = result[idx]
    idx += 1
    if pos == K:
        print(time)
        break

    for next_pos in [pos-1, pos+1, pos*2]:
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = True
            result.append((next_pos, time+1))