#파이썬의 변수 처리에 관하여
#1. 자료형을 명시할 필요가 없다.
integer_a = 3
list_a = [1,2,3]

#2. a = 3 실행 시 3이라는 정수형 객체가 메모리에 생성되고, a는 래퍼선스로 처리된다.
a = 1
b = 1
print(a is b) #is는 두 개체가 동일한지 판단하는 코드
import sys
print(sys.getrefcount(1)) #1을 가르키는 ref의 개수 리턴
c = 1
print(sys.getrefcount(1))
d = 1
print(sys.getrefcount(1))

tuple_a = 1,2,3
tuple_b = 1,2,3
print(tuple_a is tuple_b) #튜플은 객체 값 같을 시 각 래퍼런스가 동일 메모리를 가르킴
list_a = [1,2,3]
list_b = [1,2,3]
print(list_a is list_b) #리스트는 값의 변경이 가능하므로 두 리스트는 각각 다른 메모리 공간에 할당
#결론: 값의 수정이 불가능한 객체에 대해서는 하나의 메모리 공간만 할당한 뒤 변수는 래퍼런스로 처리함

# 3. 변수를 만드는 여러 방법
a,b = 'hi', 'hello'
[c,d] = ["python", "java"]
f = g = "oh"
print(a, b)
print(c,d)
print(type(c),type(d))
a, b = b , a #값 교환

# 4. 변수 해제
del a #명시적으로 해제해도 되나, 파이썬이 알아서 메모리 관리해줌

# 5. 리스트 복사
a = [1,2,3]
b = a #b는 a의 메모리 주소가 복사사됨
a[0] = 4
print(b,a is b) 

b = a[:] #값만 복사
from copy import copy
b = copy(a) # b = a[:]와 동일
print(b is a)