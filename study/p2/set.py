#집합 자료형: 리스트, 문자열, 딕셔너리, 튜플 등 iterable(반복 가능한) 객체를 쉽게 처리하기 위한 자료형
#집합 자료형 특징 : 중복 허용X, 순서 없음.
#사용처: 중복 자동 제거, 빠른 원소 탐색, 집합 연산 등에 사용

s1 = set("Hello")
print(s1) #중복 및 순서가 없어짐
#print(s1[0]) #인덱스 사용 불가

l1 = list(s1)
print(l1[0])
t1 = tuple(s1)
print(t1[1]) #리스트나 튜플로 변환 후 사용 가능

#집합 자료형 활용
s2 = set([1,2,3,4,5,6])
s3 = set([3,4,5,6,7,8])
print(s2 & s3) #교집합 연산
print(s2.intersection(s3)) #위랑 동일

print(s2|s3) #합집합 연산
print(s2.union(s3)) #위랑 동일

print(s2 - s3) #차집합
print(s2.difference(s3)) #위랑 동일

s2.add(7) #값 1개 추가하기
print(s2)

s2.update([8,9]) #값 여러개 추가
print(s2)

s2.remove(1) #특정 1개 값 제거
print(s2)

#여러 개 제거하는 법 방법: 1. remove 여러 번 쓰기, 2. 차집합 활용