n = int(input())
line = list(map(int,input().split()))
stack = []
order = 1
index = 0
while True:
    if index >= n:
        break
    if stack and stack[-1] == order:
        stack.pop()
        order += 1
    else:
        stack.append(line[index])
        index += 1

while True:
    if stack and stack[-1] == order:
        stack.pop()
        order += 1
    else:
        break

if not stack:
    print("Nice")
else:
    print("Sad")