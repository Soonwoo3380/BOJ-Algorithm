import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

def monday(m, chosen):
    if len(chosen) == m:
        print(*chosen)
        return

    for i in range(len(num_list)):
        chosen.append(num_list[i])
        monday(m, chosen)
        chosen.pop()

monday(M, [])