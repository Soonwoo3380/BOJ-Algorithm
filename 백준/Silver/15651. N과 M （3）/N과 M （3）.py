N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]

def funcky(m, chosen):
    if len(chosen) == m:
        print(*chosen)
        return
    
    for k in range(len(num_list)):
        chosen.append(num_list[k])
        funcky(m, chosen)
        chosen.pop()

funcky(M, [])