while True:
    string = input()
    stack = []
    par = ['(',')','[',']']
    result = []
    if string == '.':
        break

    for s in string:
        if s in par:
            result.append(s)

    for s in result:
        if s == '(':
            stack.append(s)
        elif s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")