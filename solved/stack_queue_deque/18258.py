import sys
import queue
def queue_command(queue, c, result): #stack이 list라고 판단되면 주소값이 복사됨. list, set, dict, 사용자 정의 클래스가 해당됨.
    if c[0] == 'push':
        queue.put(c[1])
    elif c[0] == 'pop':
        result.append(queue.get() if not queue.empty() else -1)
    elif c[0] == 'size':
        result.append(queue.qsize())
    elif c[0] == 'empty':
        result.append(1 if queue.empty() else 0)
    elif c[0] == 'front':
        result.append(queue.queue[0] if not queue.empty() else -1)
    elif c[0] == 'back':
        result.append(queue.queue[-1] if not queue.empty() else -1)

input_data = sys.stdin.read()
data = input_data.splitlines()

queue = queue.Queue()
result = []
n = int(data[0])

for i in range(1, n + 1):
    c = data[i].split()
    queue_command(queue, c, result)

print('\n'.join(map(str,result)))