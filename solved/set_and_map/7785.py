in_person = set()
n = int(input())
for _ in range(n): #O(n)
    person, log = input().split()
    if log == "enter":
        in_person.add(person) #O(1)
    elif log == "leave":
        in_person.remove(person) #O(1)
for i in sorted(list(in_person),reverse=True): #O(nlogn)
    print(i)
#전체: O(nlogn)