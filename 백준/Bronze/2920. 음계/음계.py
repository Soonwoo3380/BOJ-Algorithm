scale = list(map(int, input().split()))

result = []

for i in range(0, 6+1):
    result.append(scale[i] - scale[i+1])

result_1 = 1

for i in range(0, 6+1):
    result_1 *= result[i]

if result_1 == -1:
    print('ascending')
elif result_1== 1:
    print('descending')
else:
    print('mixed')
