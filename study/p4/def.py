#함수: 반복되는 기능을 묶어서 함수로 묶으면 좋음
def sum(a,b):
    return a + b
print(sum(3,4))

def say():
    print("Hello World") #입력, 리턴값 없음

def dif(a,b):
    print(f"{a} - {b} = {a-b}")
a = dif(4,3)
print(a) #None리턴: 아무것도 없다는 뜻

def sum_many(*args): #인수 개수가 몇 개인지 모를 때: *변수 라고 하면 됨
    sum = 0
    for a in args:
        sum += a
    return sum
print(sum_many(1,2,3,4,5))

def many(a, *b): #*앞에 인자 있으면 먼저 채감. *b, a는 오류
    sum = a
    print(a)
    for i in b:
        sum += i
    return sum
print(many(1,2,3,4,5))

def return_tuple(a, b):
    return a+b, a*b #리턴값은 언제나 한 개이기 때문에 튜플로써 리턴됨
s, m = return_tuple(3,4) #a+b는 s에 a*b는 m에 저장
print(s,m,return_tuple(5,6))

def say_myname(name, old, man = True): #인자 초기값 설정
#name, man = True, old는 오류남. 순서 지켜야함.
    print(f"이름: {name}, 나이: {old}")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myname("이종현",23) #인자 안넣을시 초기값대로 진행
say_myname("김영희",20,False) #값 넣으면 넣은 값대로 감

g = 1
def test(g):
    g = g + 1 #함수만의 지역변수임
test(g)
print(g) #2가 아닌 1출력
#해결책
def sol(g):
    return g + 1 #그냥 리턴 추천
print(sol(g))

def bad_sol():
    global g #전역변수인 g를 가져와서 사용하겠다는 의미. 별로 추천안함
    g = g + 1
bad_sol()
print(g)