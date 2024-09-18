while True:
    n = int(input())
    if(n == -1):
        break
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    divisors.pop()
    sum = 0
    for a in divisors:
        sum += a
    if(sum == n):
        print(n,end = " = ")
        for a in divisors:
            print(a,end = "")
            if(a != divisors[len(divisors)-1]):
                print(" + ",end="")
        print()
    else:
        print("{0} is NOT perfect." .format(n))


#CHAT GPT코드 : f-string과 .join을 활용하면 훨씬 간단하게 풀 수 있다. 함수를 이용하면 가독성이 훨씬 좋아진다.
def get_divisors_sum(n):
    """주어진 n의 약수들의 합을 계산합니다 (자신 제외)."""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:  # 자신을 제외한 약수
                divisors.append(i)
            if i != 1 and i != n // i and n // i != n:  # 쌍 약수
                divisors.append(n // i)
    divisors.sort()
    return divisors

def is_perfect(n):
    """n이 완전수인지 여부를 확인하고 결과를 출력합니다."""
    divisors = get_divisors_sum(n)
    if sum(divisors) == n:
        return f"{n} = {' + '.join(map(str, divisors))}"
    else:
        return f"{n} is NOT perfect."

def main():
    while True:
        n = int(input().strip())
        if n == -1:
            break
        print(is_perfect(n))

if __name__ == "__main__":
    main()