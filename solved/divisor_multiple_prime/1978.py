def is_prime_num(num):
    div = divisor(num)
    check = [1,num]
    if div == check:
        return True
    else:
        return False

def divisor(num):
    divisors = []
    for a in range(1,int(num**0.5)+1):
        if num % a == 0:
            divisors.append(a)
            if a != num // a:
                divisors.append(num//a)
    divisors.sort()
    return divisors

n = int(input())
#print(divisor(n))
#print(is_prime_num(6),is_prime_num(7))
count = 0
for a in map(int, input().split()):
    if is_prime_num(a) == True:
        count += 1
print(count)

#CHAT GPT 코드
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

N = int(input())  # 수의 개수 입력
numbers = list(map(int, input().split()))  # N개의 수 입력
prime_count = sum(1 for number in numbers if is_prime(number))
#리스트 컴프리헨션 + sum함수 활용. 근데 그냥 for문으로 해도 별차이 없음.
print(prime_count)