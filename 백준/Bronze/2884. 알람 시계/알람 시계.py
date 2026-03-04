H, M = map(int, input().split())

if M >= 45: # 45분 이상일 때, 단순히 뺀다.
    print(H, M - 45)
else: # 45분 미만일 때,
    H = H - 1 
    M = 60 + (M - 45) 
    if H < 0: # 00시 일 때, 00시 - 1시간은 23시
        H = 24 + H
    elif H == 0: # 00시는 24시로 표현하지 않는다.
        H == 0
    print(H, M)
        