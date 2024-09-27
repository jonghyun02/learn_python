n = int(input())
point = []
for i in range(n):
    x,y = map(int, input().split())
    point.append((y,x)) #순서를 바꿔서 y를 기준으로 정렬하게 함.
point.sort()

for i in range(n):
    print(point[i][1],point[i][0]) #출력은 x,y순으로