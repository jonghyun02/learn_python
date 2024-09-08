#int의 각 자리수를 뽑아내는 방법 : int형을 str로 바꾼뒤 list로 변환하면 됨.
#str을 list로 바꿀시 한 개의 요소가 list의 원소가 되는 원리를 이용 
a = 123
b = list(str(a))
print(type(a))
print(b)

c = 'abc'
d = list(c)
print(d)