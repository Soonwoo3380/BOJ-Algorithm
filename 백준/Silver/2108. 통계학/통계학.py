import sys

num_len = int(sys.stdin.readline())
num_list = []
mean = 0
med = 0
mode = 0

for iter in range(num_len):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()


# mean
for i in range(len(num_list)):
    mean += num_list[i]
print(int(round(mean/len(num_list), 0)))

# median
print(num_list[int((num_len+1)/2)-1])

if num_len == 1:
    mode = num_list[0]
else:
    prev = None
    count = 0
    max_count = 0
    modes = []

    for n in num_list:
        if n == prev:
            count += 1
        else:
            count = 1
            prev = n

        if count > max_count:
            max_count = count
            modes = [n]
        elif count == max_count:
            modes.append(n)

    modes = sorted(set(modes))

    if len(modes) == 1:
        mode = modes[0]
    else:
        mode = modes[1]

print(mode)

# range
print(abs(num_list[0] - num_list[-1]))
