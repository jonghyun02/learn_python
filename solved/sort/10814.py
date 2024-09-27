n = int(input())
person = []
for _ in range(n):
    old, name = input().split()
    old = int(old)
    person.append((old,name))
person.sort(key=lambda x:x[0])
for old, name in person: #그냥 이렇게 출력 가능.
    print(old, name)