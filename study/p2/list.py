a = ['a', 1, "a",[2,3]] #리스트 안에 어떠한 자료형도 들어갈 수 있으며 크기도 정할 필요가 없음. 그냥 개사기
print(type(a[0]),type(a[1]),type(a[2]),type(a[3])) #참고: 파이썬은 char형이 없음.

print(a[0]) #추출
b = ['b', 5]
print(a+b) #덧셈
print(a * 2) #곱셈
print(a[:2]) #슬라이싱 : list[a:b] a부터 b-1까지 추출

#값 수정
a[0] = 3
print(a) #값 한 개 수정
a[1:2] = ['a','b','c']
print(a) #범위로 수정
a[1] = ['a','b','c']
print(a) #범위로 안하고 리스트를 넣으면 리스트 그대로 들어감

#값 삭제
a[1:3] = []
print(a) #빈 리스트로 바꾸기
del a[1]
print(a) #del 키워드 이용하기

#참고: [del 객체]
x = 10
del x
# 이제 x를 사용하려고 하면 NameError가 발생합니다.
my_list = [1, 2, 3, 4]
del my_list[2:4]
print(my_list)  # 출력: [1, 2]

#리스트 함수들
a.append("HI") #push_pack이랑 동일
print(a)

c = [1,5,6,3,2]
c.sort() #자료형이 섞이면 정렬 안됨
print(c)

a.reverse() #리스트 역순으로 바꾸기
print(a)

print(a.index(3)) #인자 값이 있는 인덱스를 리턴해줌. find랑 비슷함
#print(a.index(1)) #찾는 값이 없으면 오류 발생

a.insert(2,'A') #(a,b) a번째 위치에 b라는 내용을 삽입
print(a)

a.remove('A') #처음 발견한 인자 값을 지움. 여러 개 있을 경우 하나만 지움.
print(a)

print(a.pop()) #가장 끝에 있는 요소 리턴 후 삭제
print(a)

d = [1,1,1,2,2,3]
print(d.count(1)) #해당 인자 값이 리스트 안에 몇 개 있는지 리턴

a.extend(d) #리스트에 리스트를 더하는 기능. 인자에는 리스트만 올 수 있음. a += d와 동일
print(a)

length = [1,2,3,4,5]
print(len(length)) #크기 반환

#리스트 비교
i = [1,2,3]
j = [1,2,3]
print(i==j) #애초에 [1,2,3]에 대하여 i,j는 같은 래퍼런스니깐 당연히 성립

#리스트 변수로 만들기
num = 3
n = [1,num]
print(n) #이것도 가능

#리스트 컴프리헨션
com = [a+2 for a in i if a % 2 != 0] #원래는 [] 이거 필요한데
print(com)
com = sum(a+2 for a in i if a % 2 != 0) #함수 안에 들어가면 굳이 필요없음
print(com)