a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif (a+b+c) == 180 and (a == b or b == c or c == a):
    print('Isosceles')
elif (a+b+c) == 180:
    print('Scalene')
else:
    print('Error')

#CHAT GPT코드
def classify_triangle(a, b, c):
    if a + b + c != 180: #3각 합이 180아닌 경우
        return "Error"
    
    if a == 60 and b == 60 and c == 60: #3각 같은 경우
        return "Equilateral"
    
    if a == b or b == c or a == c: #2각 같은 경우
        return "Isosceles"
    
    return "Scalene" #나머지 = 3각 합이 180이며 모든 각이 다른 경우