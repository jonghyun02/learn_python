#요약: 비어있는 자료형(ex. [],{},(),""), 숫자 0, None은 거짓.
#이를 활용해서 while, for문 등 반복문에 활용 가능

a = [1,2,3,4]
while(a):
    print(a.pop())

if[]:
    print("True")
else:
    print("False")