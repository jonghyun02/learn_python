#n(c-a1) >= a0이 모든 n>=n0에 대해 만족하도록 하는 문제
a1 , a0 = map(int,input().split()) #f(n) = a1*n + a0
c = int(input())
n0 = int(input())

if c < a1: #감소 함수는 만족X
    print(0)
elif c == a1: #기울기가 0인 경우
    if a0 <= 0: 
        print(1)
    else:
        print(0)
else: #증가함수의 경우
    if a0 <= ((c-a1)*n0):
        print(1)
    else:
        print(0)