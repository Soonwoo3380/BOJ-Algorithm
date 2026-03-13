N, M = map(int, input().split())
number_list = [i for i in range(1, N+1)]

def wow(m, start, chosen):
    if len(chosen) == m:
        print(*chosen)
        return

    for k in range(start, len(number_list)):
        chosen.append(number_list[k])
        wow(m, k+1, chosen)
        chosen.pop()

wow(M, 0, [])