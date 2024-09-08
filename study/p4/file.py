#github workspace 기본 위치: /workspaces/learn_python - pwd 명령어 쓰면 확인 가능

#'r' : 읽기모드 - 파일의 내용을 읽기만 할 때 사용. open함수의 default모드
#'w' : 쓰기모드 - 해당 파일이 존재할 경우 모든 내용을 지움. 없을 시 새로 파일 생성
#'a' : 추가모드 - 기존 파일의 내용을 유지하며 내용 추가

#새로운 파일 생성
w = open("study/p4/file_test/write_mode.txt",'w') #해당 위치에 쓰기모드 적용
for i in range(1,11):
    data = f"쓰기모드 {i}번째 줄입니다.\n"
    w.write(data)
w.close() #파일 객체를 닫음. 파이썬은 프로그램 종료 시 자동 실행됨
#써야 하는 이유 : 중간에 안닫고 파일 다시 열려고 하면 오류가 발생하기에 써주는 것이 좋음

for i in range(1,11):
    data = f"{i}번째 줄입니다.\n"
    print(data)
#f.write()와 print()차이는 파일에 출력하냐 모니터에 출력하냐의 차이 뿐이다. write()를 완전 새로운 함수로 보지 말고 print()다라는 생각으로 접근하자



#프로그램 외부에 저장된 파일 내용 불러오기
r = open("study/p4/file_test/read_mode.txt",'r') #해당 위치에 읽기모드 적용
while True:
    line = r.readline() #파일의 한 줄을 읽어옴. 더 이상 읽을게 없을 시 None리턴
    if not line:
        break
    print(line)
r.close()

# while True:
#     line = input()
#     if not line:
#         break
#     print(line)
#readline()이나 input() 차이는 그저 파일에서 읽냐 키보드로 읽냐의 차이일 뿐이다.

r = open("study/p4/file_test/read_mode.txt",'r') #해당 위치에 읽기모드 적용
line = r.readlines() #파일의 모든 내용을 받아 각각의 줄을 리스트의 요소로 반환함
for i in line:
    print(i)
r.close()

r = open("study/p4/file_test/read_mode.txt",'r') #해당 위치에 읽기모드 적용
data = r.read() #파일의 모든 내용을 문자열로 받음
print(data)
r.close()



#파일에 새로운 내용 추가
a = open("study/p4/file_test/add_mode.txt",'a') #해당 위치에 추가모드 적용
for i in range(11,16):
    data = f"새로 추가된 {i}번째 줄입니다.\n"
    a.write(data)
a.close()

#with문
with open('study/p4/file_test/with.txt', 'r') as file:
    content = file.read()
    print(content)