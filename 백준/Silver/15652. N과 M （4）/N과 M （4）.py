import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]

def n_m(m, start, chosen):
    if len(chosen) == m:
        print(*chosen)
        return
    
    for k in range(start, len(num_list)):
        chosen.append(num_list[k])
        n_m(m, k, chosen)
        chosen.pop()
     
n_m(M, 0, [])