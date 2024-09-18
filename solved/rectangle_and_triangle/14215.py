a = list(map(int,input().split()))

def classify_triangle(a):
    a.sort()
    if a[0] + a[1] <= a[2]:
        return 2*(a[0]+a[1])-1
    else:
        return a[0]+a[1]+a[2]

print(classify_triangle(a))

#CHAT GPT코드
#[a,b,c]로 직접 리스트 만들어도 됨
def max_perimeter(a, b, c):
    # 삼각형의 세 변을 정렬
    x, y, z = sorted([a, b, c])
    
    # 삼각형 부등식이 만족될 경우
    if x + y > z:
        return x + y + z
    else:
        # 삼각형을 만들기 위해 가장 큰 변의 길이를 조정
        return 2 * (x + y) - 1

# 입력 받기
a, b, c = map(int, input().split())

# 결과 출력
print(max_perimeter(a, b, c))
