import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = int(matrix[i][j])


from collections import deque

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
dq = deque()
dq.append((0,0,0))

while dq:
    col, row, k = dq.popleft()

    if (col, row) == (N-1, M-1):
        print(visited[col][row][k])
        break
    
    for (nx, ny) in [(col+1, row), (col, row+1), (col-1, row), (col, row-1)]:
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        if visited[nx][ny][k] == 0 and matrix[nx][ny] == 0:
            visited[nx][ny][k] = visited[col][row][k] + 1
            dq.append((nx, ny, k))

        if matrix[nx][ny] == 1 and k ==0 and visited[nx][ny][1] == 0:
            visited[nx][ny][1] = visited[col][row][0] + 1
            dq.append((nx, ny, 1))

else:
    print(-1)




