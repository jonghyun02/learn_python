def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

n = int(input())
num = [int(input()) for _ in range(n)]
for i in num:
    while True:
        if is_prime(i):
            print(i)
            break
        i += 1