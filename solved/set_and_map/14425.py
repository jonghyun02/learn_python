n,m = map(int, input().split())
s = set([input() for _ in range(n)]) #O(n)
check = [input() for _ in range(m)]
count = 0
for i in check: #O(m)
    if i in s:
        count += 1
print(count)
#전체: O(m+n)