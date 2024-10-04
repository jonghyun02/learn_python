class Stack:
    def __init__(self):
        self.items = []  # 스택을 저장할 리스트
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)  # 요소를 스택의 맨 위에 추가
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def __str__(self):
        return str(self.items)

stack = Stack()
k = int(input())
for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.push(n)
print(sum(stack))