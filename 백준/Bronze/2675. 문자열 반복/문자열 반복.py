T = int(input())


for _ in range(T):
    result = ''
    R, S = input().split()
        
    for i in range(len(S)):
        result += S[i] * int(R)
        
    print(result)        