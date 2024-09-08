M = int(input())
N = int(input())

def is_prime(num):
    if num <= 1: #1거르기
        return False
    if num == 2: #2포함
        return True
    if num % 2 == 0: #짝수 전부 제외
        return False
    for i in range(3, int(num**0.5) + 1, 2): 
        #약수 대칭 성질 이용해서 num**0.5 + 1, 짝수 체크할 필요 없어서 ,2
        if num % i == 0:
            return False
    return True

min = 0
total = 0
for i in range(M, N+1):
    if is_prime(i):
        if min == 0:
            min = i
        total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(min)


#CHAT GPT코드
# 소수 판별 함수 정의
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
M = int(input())
N = int(input())

# 소수 리스트 생성
primes = []

for i in range(M, N + 1):
    if is_prime(i):
        primes.append(i)

# 결과 출력
if primes:
    print(sum(primes))  # 소수의 합
    print(primes[0])    # 소수 중 최솟값
else:
    print(-1)