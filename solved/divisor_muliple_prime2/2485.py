def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
tree = [int(input()) for _ in range(n)]
gap = [tree[i+1]-tree[i] for i in range(n-1)]

mgcd = gap[0]
for i in range(len(gap)-1):
    mgcd = gcd(mgcd,gap[i+1])
count = 0
for i in range(len(gap)):
    count += gap[i] // mgcd - 1
print(count)

#n개에 대한 최대공약수를 구해달라는 문제.
#n개에 대한 최대공약수: a,b,c,d... 가 있을 때 a,b로 구한 최대공약수 d가 있으면 d,c에 대한 최대공약수를 구하고... 반복