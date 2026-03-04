input_list = list(input())

idx = 0
for i in range(len(input_list)):
    if input_list[i] == '*':
        input_list[i] = 0
        idx = i
    else:
        input_list[i] = int(input_list[i])

for j in range(len(input_list)):
    if (j+1) % 2 == 0:
        input_list[j] = input_list[j] * 3

sum = 0
for k in range(len(input_list)):
    sum += input_list[k]

weight = 3 if (idx+1) % 2 == 0 else 1

for x in range(10):
    if (sum + x * weight) % 10 == 0:
        print(x)
        break