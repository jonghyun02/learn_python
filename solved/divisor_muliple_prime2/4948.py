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

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1,2*n+1):
        if is_prime(i):
            count += 1
    print(count)