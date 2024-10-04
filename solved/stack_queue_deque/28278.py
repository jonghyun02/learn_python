import sys

def stack_command(stack, c, result): #stack이 list라고 판단되면 주소값이 복사됨. list, set, dict, 사용자 정의 클래스가 해당됨.
    if c[0] == '1':
        stack.append(c[1])
    elif c[0] == '2':
        result.append(stack.pop() if stack else -1)
    elif c[0] == '3':
        result.append(len(stack))
    elif c[0] == '4':
        result.append(0 if stack else 1)
    elif c[0] == '5':
        result.append(stack[-1] if stack else -1)
#print연산 여러 번 호출이 시간을 많이 잡아먹기에 모아서 한 번에 출력

# sys.stdin.read를 사용하여 모든 입력을 한 번에 읽기
input_data = sys.stdin.read() #EOF까지 입력받음. win기준 Ctrl + Z, Linux기준 Ctrl + D
data = input_data.splitlines() #줄단위로 문자열을 리스트로 변환

stack = []
result = []
n = int(data[0])  # 첫 번째 줄에서 명령 수를 읽음

for i in range(1, n + 1):
    c = data[i].split()
    stack_command(stack, c, result)

print('\n'.join(map(str,result))) #join은 원래 문자열에만 사용가능한데, map으로 str적용 시 사용가능.