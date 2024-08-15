#for문: for a in b로 구성되며 b에는 리스트, 튜플, 딕셔너리, 문자열 등 반복 가능한 객체가 들어갈 수 있음.
a = [('a',1),('b',2),('c',3)]
for one, two in a: #a의 형태에 맞춰서 조절 가능
    print(one,two)

my_dict = {'a': 1, 'b': 2}
for key in my_dict: #기본적으로 딕셔너리 사용시 key값만 출력 가능.
    print(key)  # a, b

for value in my_dict.values(): #이런 식으로 vales나 items활용해야 value도 출력 가능.
    print(value)  # 출력: 1, 2

for a in range(1,8,2): #range함수 구성 (a,b,c), a: 시작, b: 끝, c: 증가 수치, a ~ b-1까지 c만큼 증가하며 반복. 
    print(a, end = " ") # end = " " -> 줄바꿈 방지

for a in range(4): #a,c생략 시 a = 0, c = 1로 디폴트.
    print(a, end = " ")
print()

#구구단 만들기
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print()

#리스트 안에 for문 넣기
a = [1,2,3,4]
result = []
for num in a:
    if(num % 2 == 0):
        result.append(num*3) #1번 코드
print(result) 

result = [num*3 for num in a if num % 2 == 0] #1번 코드랑 동일한 결과
print(result)
#기본식: 리스트 = [표현식 for 항목 in 반복 가능 객체 if 조건문]