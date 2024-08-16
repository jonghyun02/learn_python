#map함수: map(function, iterator1, iterator2...) 함수와 함수의 인자 개수와 동일한 인자를 리스트 같은 반복가능한 개체로 받고 각 함수가 적용된 결과를 map 객체로 리턴하는 함수

a = [1,2,3]
def double(a):
    return a**2
test = map(double, a) #map이 저장된 메모리 주소 리턴
list_trans = list(test) #사용하려면 변환 작업 거쳐야함
print(test)
print(type(test)) #map 클래스
print(list_trans)

a1 = [1,2,3,4]
a2 = [1,2,3,4,5]
def sum(a,b):
    return a+b
test2 = tuple(map(sum, a1, a2)) #함수 인자에 맞게 구성. 인자 개수 최소값만큼 실행됨
print(test2)

a , b = map(int, input().split()) #공백으로 들어오는 입력값 이런 식으로 처리 가능
print(a,b)