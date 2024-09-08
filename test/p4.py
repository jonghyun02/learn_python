#함수
#Q1
n = int(input())
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
print(fib(n))


#파일 읽고 쓰기
#Q1
f = open('test/sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / len(lines) #len() 리스트 길이 리턴

f = open('test/result.txt','w')
f.write(str(average)) #write객체는 str만 사용 가능
f.close()