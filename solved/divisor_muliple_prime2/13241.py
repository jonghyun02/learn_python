def gcd(a, b):
    while b:
        a, b = b, a % b #a = bq + c -> b = cq + d ... 나누어 떨어질 때까지 반복, 여기서 q는 몫
    return a

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
sum_n = n1*d2 + n2*d1
sum_d = d1*d2
ifn = sum_n // gcd(sum_n,sum_d)
ifd = sum_d // gcd(sum_n,sum_d)
print(ifn, ifd)

"""
n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
sum_n = n1 * d2 // gcd(d1, d2) + n2 * d1 // gcd(d1, d2)
sum_d = lcm(d1, d2)
처음에 이렇게 했는데, 1/2 2/4 하니깐 제대로 약분 안됨. 그냥 다 계산하고 마지막에 약분하는게 맞는듯
"""