n = int(input())
x = []
y = []
for a in range(n):
    point = list(map(int,input().split()))
    for i in  range(0,3,2):
        x.append(point[i])
        y.append(point[i+1])
    cost = 2 * ((max(x) - min(x)) + (max(y) - min(y)))
    print(cost)