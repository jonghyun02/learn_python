def classify_triangle(a):
    a.sort()
    if a[2] >= a[0]+a[1]:
        return "Invalid"
    
    if a[0] == a[1] and a[1] == a[2]:
        return "Equilateral"
    
    if a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        return "Isosceles"
    
    return "Scalene"

while True:
    a = list(map(int,input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    else:
        print(classify_triangle(a))


#CHAT GPT코드
#굳이 sort하는 것보다 a+b>c, b+c>a, a+c>b 세 조건을 모두 만족해야 삼각형이다 라는 것을 활용하는게 훨씬 효율적인 코드임.
#sort자체가 O(NlogN)이다보니 더 적은 복잡도가 가능하면 무조건 그거로 가는게 맞음
def classify_triangle(a, b, c):
    # 삼각형 유효성 검사
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    
    # Equilateral 검사
    if a == b == c:
        return "Equilateral"
    
    # Isosceles 검사
    if a == b or a == c or b == c:
        return "Isosceles"
    
    # Scalene
    return "Scalene"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    results = []
    for line in data:
        a, b, c = map(int, line.split())
        if a == 0 and b == 0 and c == 0:
            break
        results.append(classify_triangle(a, b, c))
    
    for result in results:
        print(result)
