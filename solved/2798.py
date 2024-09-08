n, m = map(int, input().split())
num = list(map(int, input().split()))
max = 0
sum = 0
for i in range(n-2):
    sum += num[i]
    for j in range(i+1,n-1):
        sum += num[j]
        for k in range(j+1,n):
            sum += num[k]
            if sum <= m and sum > max:
                max = sum
            sum -= num[k]
        sum -= num[j]
    sum -= num[i]
print(max)

#CHAT GPT 코드: 그냥 대입 연산자 쓰면 되는데 생각을 너무 많이 했다
# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

best_sum = 0

# 세 개의 카드를 고르는 3중 반복문
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            # M을 넘지 않으면서 최대한 가까운 합을 찾는다.
            if current_sum <= M:
                best_sum = max(best_sum, current_sum)

print(best_sum)

#CHAT GPT 코드2 : 모든 조합을 리턴해주는 함수 combinations 사용
from itertools import combinations

# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 가능한 모든 3장의 카드 조합을 만든다.
best_sum = 0
for comb in combinations(cards, 3):
    current_sum = sum(comb)
    # M을 넘지 않으면서 최대한 가까운 합을 찾는다.
    if current_sum <= M:
        best_sum = max(best_sum, current_sum)

print(best_sum)