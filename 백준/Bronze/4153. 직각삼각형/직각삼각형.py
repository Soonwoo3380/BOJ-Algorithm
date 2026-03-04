while True:
    A, B, C = map(int, input().split())
    sort_list = sorted([A,B,C])

    if sort_list == [0,0,0]:
        break

    if sort_list[0]**2 + sort_list[1]**2 == sort_list[2]**2:
        print('right')
    else:
        print('wrong')
