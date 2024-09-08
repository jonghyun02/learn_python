#입력
a = input("값 입력하기 : ")
print("a값: ",a)

a,b = map(int, input().split()) #int로 변환
c,d = input().split() #그냥 입력 받을시 str로 받음
print(type(a),type(b))
print(a+b)
print(type(c),type(d))
print(c+d)


#출력
print("a" "b""c") #그대로 abc출력
print("a"+"b"+"c") #위랑 동일
print("a","b","c") #a b c로 공백 포함 출력
print("con",end=" ") #다음 print가 같은 줄에 출력됨
print("tinue") 