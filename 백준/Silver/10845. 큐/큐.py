import sys
input = sys.stdin.readline

N = int(input())

que = []

for _ in range(N):
    command = input().split()

    if command[0]=='push':
        value = int(command[1])
        que.append(value)
    
    elif command[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.pop(0)

    elif command[0] =='size':
        print(len(que))

    elif command[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    
    elif command[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])