n = int(input())

def digit(n):
    for i in range(1,100):
        if n // 10**i == 0:
            return i #자리수 리턴. ex) 3->1, 12->2

def div_sum(n):
    d = []
    d.append(n%10)
    for i in range(1,digit(n)):
        d.append((n//10**i)%10)
    return n+sum(d) #분해합

check = False
for i in range(1,n):
    if div_sum(i) == n:
        print(i)
        check = True
        break

if not check:
    print(0)

#CHAT GPT 코드 : int의 각 자리수를 뽑아내는 방법 익혀두길.
def find_constructor(n):
    for i in range(1, n + 1):
        decomposition_sum = i + sum(map(int, str(i)))
        if decomposition_sum == n:
            return i
    return 0

n = int(input())
print(find_constructor(n))