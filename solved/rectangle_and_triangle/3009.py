x = []
y = []
for i in range(0,3):
    a, b = map(str,input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
if x[0] == x[1]:
    print(x[2], end=' ')
else:
    print(x[0], end=' ')
if y[0] == y[1]:
    print(y[2], end=' ')
else:
    print(y[0], end=' ')