import sys
input = sys.stdin.readline


M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]


queue = []
head = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

while head < len(queue):
    (x, y) = queue[head]
    head += 1

    for (nx, ny) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if box[nx][ny] != 0:
            continue

        box[nx][ny] = box[x][y] + 1
        queue.append((nx, ny))



for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, box[i][j])

print(result-1)
