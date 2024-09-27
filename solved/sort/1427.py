n = input()
num = [i for i in n] #지금은 n값 그대로 list로 바꿀거라 num = list(n)으로 해도 똑같음
num.sort()
num.reverse() #num.sort(reverse=True)하면 똑같은 기능. 기본적으로 (reverse=False)임.
for i in num:
    print(i,end='')


#CHAT GPT코드: sort()에 인자가 있다. str을 list함수로 변환하면 [i for i in n] 이거랑 똑같음.
def sort_digits_descending(number):
    # 숫자를 문자열로 변환
    num_str = str(number)
    # 각 자리수를 리스트로 변환
    digits = list(num_str)
    # 리스트를 내림차순으로 정렬
    digits.sort(reverse=True)
    # 정렬된 리스트를 문자열로 결합
    sorted_num_str = ''.join(digits)
    return sorted_num_str

# 입력 받기
N = int(input().strip())
# 자리수를 내림차순으로 정렬한 결과 출력
print(sort_digits_descending(N))
