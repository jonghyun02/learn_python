n = int(input())
point = list(map(int,input().split()))
compare = sorted(list(set(point)))

for i in point:
    print(compare.index(i), end=" ")
#이거 시간초과로 틀림. index() 시간 복잡도가 O(N^2)이라서.


#CHAT GPT가 짠 코드: index딕셔너리를 직접 만들어서 코드의 시간 복잡도를 줄임. enmerate는 O(N)
n = int(input())
point = list(map(int, input().split()))

# 중복을 제거하고 정렬한 점수 리스트
compare = sorted(set(point))

# 점수와 인덱스를 매핑한 딕셔너리 생성
rank = {value: index for index, value in enumerate(compare)}

# 각 점수의 랭크를 출력
for i in point:
    print(rank[i], end=" ")