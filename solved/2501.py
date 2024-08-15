N,K = map(int, input().split())
n = []
for a in range(1,N+1):
    if(N % a == 0):
        n.append(a)

if K > len(n):
    print(0)
else:
    print(n[K-1])

#CHAT GPT코드: 약수는 늘 짝을 이룬다는 것 + 둘 중 하나는 무조건 N의 제곱근 이하의 정수다라는 사실을 이용함
# 입력 받기
N, K = map(int, input().split())

# 약수를 저장할 리스트
divisors = []

# N의 약수를 찾기
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)

# 약수를 정렬
divisors.sort()

# K번째 약수 출력 (1-based index이므로 K-1)
if K <= len(divisors):
    print(divisors[K-1])
else:
    print(0)