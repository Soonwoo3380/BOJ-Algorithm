import sys
input = sys.stdin.readline

N = int(input())

input_list = []
for _ in range(N):
    input_list.append(int(input()))


num_list = [0] * N
for m in range(N):
    num_list[m] = m+1


possible = True
Max_Verstappen = input_list[0]


result_list = []


for _ in range(Max_Verstappen):
    result_list.append('+')
result_list.append('-')


for i in range(1, N):
    if Max_Verstappen > input_list[i]:
        result_list.append('-')
    elif Max_Verstappen < input_list[i]:
        for _ in range(input_list[i]-Max_Verstappen):
            result_list.append('+')
        result_list.append('-') 
        Max_Verstappen = input_list[i]

num_list_2 = []
compare_list = []
on_going = 0
for i in range(len(result_list)):
    if result_list[i] == '+':
        on_going += 1
        num_list_2.append(on_going)
    elif result_list[i] == '-':
        compare_list.append(num_list_2[-1])
        num_list_2.pop()

is_valid = True

for y in range(N):
    if compare_list[y] != input_list[y]:
        print('NO')
        is_valid = False
        break

if is_valid:
    for s in result_list:
        print(s)