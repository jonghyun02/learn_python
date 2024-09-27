tmp = set()
tmp.add((1,2))
tmp.add((1,2))
print(tmp)
class ClassA:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, ClassA):
            return ClassA(self.value + other.value)
        elif isinstance(other, ClassB):
            return ClassA(self.value + other.value)  # ClassA로 반환
        return NotImplemented  # 다른 타입일 경우

class ClassB:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, ClassA):
            return ClassB(self.value + other.value)  # ClassB로 반환
        elif isinstance(other, ClassB):
            return ClassB(self.value + other.value)
        return NotImplemented  # 다른 타입일 경우

# 인스턴스 생성
a = ClassA(5)
b = ClassB(10)

# a + b (a.__add__(b) 호출)
result1 = a + b  # ClassA의 __add__ 호출
print(result1.value)  # 출력: 15

# b + a (b.__add__(a) 호출)
result2 = b + a  # ClassB의 __add__ 호출
print(result2.value)  # 출력: 15
