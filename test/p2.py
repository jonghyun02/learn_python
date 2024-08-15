#문자열
#Q1
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
#Q2
print(pin[7])

#리스트
#Q1
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
#Q2
a = ['Life','is','too','short']
result = " ".join(a) #문자열에 사용 시 각 문자 사이, 리스트에 사용 시 각 요소 사이
print(result)

#튜플
#Q1
a = (1,2,3)
a += (4,) #튜플은 튜플끼리만 더하기 가능함, 요소 한 개라 , 붙여야함
#실제로는 4가 포함된 튜플을 새로 만든 후에 대입하는거임
print(a)

#딕셔너리
#Q1
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') #딕셔너리 pop 사용시 value 리턴
print(a)
print(result)
#print(a.pop(70)) #key만 사용가능

#집합
#Q1
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#변수
#Q1
#b는 a랑 같은 [1,2,3] 리스트 객체를 가르키고 있기 때문