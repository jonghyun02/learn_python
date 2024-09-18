num = [int(input()) for _ in range(5)]
num.sort()
avg = (num[0] + num[1] + num[2] + num[3] + num[4]) // 5
mid = num[2]
print(avg)
print(mid)