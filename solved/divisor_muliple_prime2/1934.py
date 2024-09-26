def divisor(N):
    divisors = set()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors.add(i)
            divisors.add(N // i)
    return divisors

def greatest_common_divisor(a,b):
    return sorted(list(divisor(a) & divisor(b)))[-1]

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    gcd = greatest_common_divisor(a,b) #최대공약수
    lcm = a*b//gcd #최소공배수
    print(lcm)

#CHAT GPT가 짜준 코드: 최대공약수는 유클리드 호제법으로 구함.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
results = []

for i in range(T):
    A, B = map(int, input().split())
    results.append(lcm(A, B))