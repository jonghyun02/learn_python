#튜플의 특징. 값의 삭제 및 수정이 불가능하다. const된 리스트 같은 느낌

#생성 방법
t1 = () #빈 튜플
t2 = (1,) #한 가지 요소만 있을 경우 반드시 ,를 붙여야함.
t3 = (1) #안붙일 경우 튜플이 아니라 다른 자료형이 됨.
t4 = 1,2,3 #괄호 생략 가능

print(type(t2))
print(type(t3))
print(type(t4))

#del t2[0] #삭제가 불가능하므로 오류 발생
#t2[0] = 2 #수정도 불가능하므로 오류 발생

#가능한 연산
print(t4[0]) #추출
print(t4[0:2]) #슬라이싱
print(t4 + (1,2)) #더하기
print(t4 * 2) #곱셈