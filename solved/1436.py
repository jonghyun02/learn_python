n = int(input())

order = 0
num = 666
while True:
    if str(num).find('666') != -1:
        order += 1
        if order == n:
            print(num)
            break
        num += 1
    else:
        num += 1


#CHAT GPT코드: 그냥 서브 문자열이 포함되어있나만 체크하고 싶으면 in을 쓰면 된다. 내 코드 num += 1 한 번 낭비했다.
def find_nth_end_of_world_number(N):
    count = 0
    current_number = 666

    while True:
        # 현재 숫자를 문자열로 변환하여 '666'이 포함되어 있는지 검사
        if '666' in str(current_number):
            count += 1
            # N번째 숫자를 찾았으면 반환
            if count == N:
                return current_number
        current_number += 1

# 입력을 받음
N = int(input().strip())
# N번째 종말의 숫자를 찾아서 출력
print(find_nth_end_of_world_number(N))