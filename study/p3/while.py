number = 0
while not number:
    number = int(input())
    print("number",number)

a = 10
b = 5
while a < 10:
    if(a % 2 == 0):
        continue
    print("악")
    a -= 1 #파이썬은 a++, a--가 없음
    
    if(b < 5):
        break

while True:
    print("Ctrl + C 누르면 탈출 가능")