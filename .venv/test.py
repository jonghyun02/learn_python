a = "I'm learning python python python"

print(a[0]) #문자 추출 가능. C++과 달리 str형으로 추출됨.
print(a[-1]) #맨끝 인덱스 -1로 표현 가능
print(a[0:4]) #문자열 슬라이싱 가능. substr이랑 같은 역할. [a:b] a부터 'b-1'까지 출력
print(a[20:-1]) #마이너스 인덱스 활용 가능
print(a[:4]) #슬라이싱

print("I'm learning %s" %"python") #c언어처럼 문자열 포멧팅 가능
print("%-10d I'm learning %10d" %(123,456)) #10칸 공백을 만들고 오른쪽부터 채운다는 의미. -10일시 왼쪽부터 채움.
print("I'm learning %10.4f" %3.1456789) #%10.4f -> 10칸 공백을 만들고 소수점은 4자리까지만 출력하며 오른쪽부터 채움.

print(a.count("python")) #매게변수 안에 있는 값이 몇 번 나오는지 리턴
print(a.count("python",14)) #탐색 시작위치 설정 가능
print(a.count("python",14,20)) #시작과 끝위치 둘 다 설정 가능, 없으면 0리턴

print(a.find("python")) #가장 먼저 발견된 문자의 인덱스 리턴
print(a.find("python",14)) #탐색 시작위치 설정 가능
print(a.find("python",14,20)) #시작과 끝위치 둘 다 설정 가능, 찾는 값이 없을 시 -1리턴

print(a.index("python",13,20)) #find랑 다 똑같은데, 없을시 -1리턴이 아닌 오류를 일으킨다는 점이 다름.
#print(a.index("python",14,20)) #못찾아서 오류남

b = "A"
print(b.join("abcd"))