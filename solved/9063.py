n = int(input())
x = []
y = []
for i in range(0,n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
area = (x[n-1] - x[0]) * (y[n-1] - y[0])
print(area)

#CHAT GPT코드
import sys

def find_rectangle_area(points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    points = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(N)]
    
    area = find_rectangle_area(points)
    print(area)

if __name__ == "__main__":
    main()
