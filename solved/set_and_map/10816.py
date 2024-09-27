n = int(input())
n_num = {}
for i in map(int, input().split()):
    if i in n_num:
        n_num[i] += 1
    else:
        n_num[i] = 1
m = int(input())
for i in map(int, input().split()):
    if i in n_num:
        print(n_num[i], end=" ")
    else:
        print(0, end=" ")