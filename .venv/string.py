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
print(b.join("abcd")) #b안에 있는 문자를 사이사이에 넣음. 출력해서 확인하도록.

c="hello"
print(c.upper()) #대문자 변환

d = "HI"
print(d.lower()) #소문자 변환

e = "   SPACE_REMOVE    "
print(e.lstrip()) #왼쪽 공백 제거
print(e.rstrip()) #오른쪽 공백 제거
print(e.strip()) #양쪽 공백 제거

print(a.replace("python","string")) #(a,b) a: 찾을 문자열, b: 바꿀 문자열. C++ replace는 한 번만 바꾸고 불편하지만 이건 찾은 문자열 전부를 바꿔버리며 사용법이 굉장히 간단함. 
#C++: string find_str = "python"; a.replace(a.find(find_str), find_str.length(), "string");
print(a.replace("python","string",1)) #세 번째 인자로 바꿀 횟수 설정도 가능함.

print(a.split()) #문자열을 리스트로 변환함. 인자 값 없을 시 공백을 기준으로 함.
f = "std::string::find"
print(f.split("::")) #인자 값을 넣을 시 그 값을 기준으로 나눔.
print(f.split(":")) #해당 인자 값이 나올 때까지를 기준으로 나누는 듯.

#또 다른 포멧팅 기법
print("I'm {0} testing {1} format function" .format("wow",3)) #인덱스로 넣기
g = "wow"
f = 3
print("I'm {0} testing {1} format function" .format(g,f)) #변수로 넣기
print("I'm {hello} testing {hi} format function" .format(hello="oh",hi=3)) #이름으로 넣기
print("{0:<10}" .format("hi")) #공백 10칸 만들고 왼쪽 정렬 포멧팅
print("{0:>10}" .format("hi")) #공백 10칸 만들고 오른쪽 정렬 포멧팅
print("{0:^10}" .format("hi")) #공백 10칸 만들고 가운데 정렬 포멧팅
print("{0:!^10}" .format("hi")) #공백 10칸 만들고 가운데 정렬 및 !로 공백 채우는 포멧팅
print("{day:10.4f}" .format(day = 3.145678)) #%10.f랑 똑같음
print("{0}{{and}}" .format("wow")) #포멧팅 함수가 있는데 {} 출력하고 싶으면 {{}} 이렇게 쓰면 됨