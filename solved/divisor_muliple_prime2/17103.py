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

T = int(input())
num = sorted([int(input()) for _ in range(T)])
prime_num = set()
prime_num.add(2)
for i in range(3,len(num),2):
    prime_num.add(i)
    
for i in range(T):
    gold_partition = 0
    if is_prime(2) and is_prime(num[i]-2):
        gold_partition += 1
    for j in range(3,num[i]//2+1,2):
        if is_prime(j) and is_prime(num[i]-j):
            gold_partition += 1
    print(gold_partition)