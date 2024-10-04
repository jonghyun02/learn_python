def eratosthenes(num:int = 1000000):
    MAX = num + 1 #num까지 검사하려고 +1
    LIM = int(num ** 0.5) + 1 #
    RSET = lambda strt, end, gap: set(range(strt, end, gap))
    
    # 5 (mod 6)과 1 (mod 6)을 참으로 설정한다. 이들은 2의 배수도 아니고 3의 배수도 아닌 숫자집합이다.
    # 단, 1은 소수가 아니기에 1 (mod 6)은 7부터 시작한다.
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3) # 3 추가
    if num > 1: prime.add(2) # 2 추가
    for i in range(5, LIM, 6):
        # 5 (mod 6) 부분
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
            #i
        # 1 (mod 6) 부분
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)
    return prime

T = int(input())
num = [int(input()) for _ in range(T)]
prime = eratosthenes(max(num))
for n in num:
    gold_partition = 0
    if 2 in prime and n-2 in prime:
        gold_partition += 1
    for i in range(3, n//2+1,2):
        if i in prime and n-i in prime:
            gold_partition += 1
    print(gold_partition)

#에라토스테네스의 체 공부하기: 특정 범위 내 소수를 판정할 때 가장 빠른 알고리즘