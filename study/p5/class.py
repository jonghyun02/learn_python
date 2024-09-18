#왜 클래스를 쓰는 것일까?
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))
#두 개의 계산기를 운용하고 싶은 경우, 클래스를 사용하지 않을 시 함수를 두 개 만들어야한다.
#만일 3개, 5개 그 이상의 계산기가 필요하다면?.. 굉장히 비효율적이다


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
#쿨래스 사용 후 굳이 추가적인 코드 작업 없이도 여러 개의 계산기를 운용할 수 있게 됐다.


#클래스 사용법
class Service:
    secret = "오늘은 24.9.8"
    def __init__(self,name): #__init__은 인스턴스 생성 시 항상 실행된다.
        self.name = name #self.name은 인스턴스 변수라 인스턴스가 살아있는 동안 인스턴스 내에서 유지된다.
    def sum(self,a,b): #클래스 메서드에는 self가 있어야 한다. self는 인스턴스를 의미
        result = a + b
        print(f"{self.name}님의 {a}+{b}={result}입니다.")
    
jong = Service("이종현") #__init__에 의해 인수를 넣어야 한다.
print(jong.secret) #클래스의 함수나 변수에 접근 시 .을 붙여야 한다.
jong.sum(1,2) #jong.sum(jong,1,2) 또는 Service.sum(jong,1,2)과 같다.
#self는 파이썬이 알아서 생략해주는 것이다.


#실전! 사칙연산 클래스 만들기
class FourCal:
    def setdata(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b
    def sub(self):
        return self.a - self.b
    def div(self):
        return self.a // self.b

a = FourCal()
a.setdata(4,2)
print(a.a, a.b) #self인수 부분에 인스턴스가 들어가는 것이 맞는지 확인
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())


#실전2! 박씨네 집 클래스 만들기
class HousePark:
    lastname = "박" #클래스 변수라 모든 인스턴스에 대해 동일한 값을 가짐
    def __init__(self,name):
        self.fullname = self.lastname + name 
    def travel(self,where):
        print(f"{self.fullname}, {where}여행을 가다.")
    
pey = HousePark("종현")
pey.travel("서울")


#클래스 상속: class a(b) a가 b를 상속받는다.
class HouseKim(HousePark):
    lastname = "김" #같은 이름인 lastname만 "박"->"김"으로 바뀌고 모든 기능을 그대로 받는다.
    def travel(self, where, day): #메서드 오버라이딩: 같은 이름을 가진 메서드를 다시 정의함
        print(f"{self.fullname}, {where}여행 {day}일 가네.")

bab = HouseKim("밥")
bab.travel("대구", 3)


#연산자 오버로딩
class HousePark:
    lastname = "박" #클래스 변수라 모든 인스턴스에 대해 동일한 값을 가짐
    def __init__(self,name):
        self.fullname = self.lastname + name 
    def travel(self,where):
        print(f"{self.fullname}, {where}여행을 가다.")
    def __add__(self,other): #other가 다른 인스턴스
        print(f"{self.fullname}, {other.fullname} 같이 여행갔네")

class HouseKim(HousePark):
    lastname = "김" #같은 이름인 lastname만 "박"->"김"으로 바뀌고 모든 기능을 그대로 받는다.
    def travel(self, where, day): #메서드 오버라이딩: 같은 이름을 가진 메서드를 다시 정의함
        print(f"{self.fullname}, {where}여행 {day}일 가네.")
    def __add__(self,other): #other가 다른 인스턴스
        print(f"{self.fullname}, {other.fullname} 같이 결혼했네")

jong = HousePark("종현")
bab = HouseKim("밥")
jong + bab #jong.__adder__(bab)과 같음
bab + jong #bab.__adder__(jong)과 같음

class overload:
    def __init__(self,num):
        self.num = num
        print(type(num))
    def __add__(self,num):
        print(f"자신의 인스턴스가 연산 왼쪽에 있는 경우 __add__불러와짐 {self.num}+{num}={self.num+num}")
    def __radd__(self,num):
        print(f"자신의 인스턴스가 연산 오른쪽에 있는 경우 __radd__ 불러와짐 {num}+{self.num}={self.num+num}")

test = overload(10)
test + 20 
30 + test #radd불러와짐. radd 없으면 오류 발생