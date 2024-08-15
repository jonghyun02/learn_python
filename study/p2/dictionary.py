#딕셔너리. key와 value로 구성된 자료형. c++ map이랑 비슷함.

dic = {'Key':'Value'} #{}와 key, value로 구성되어 있음

a = {1:'a'}
a[2] = 'b' #중요! 딕셔너리는 순서가 존재하지 않음
print(a)

#딕셔너리 중요 특징
#1. 키 값은 중복되면 안된다.
b = {1:'a', 1:'b', 1:'c'}
print(b[1]) # 어떤 값이 불러와질지는 아무도 모른다.

#2. key에 튜플은 들어갈 수 있으나 리스트나 딕셔너리는 들어갈 수 없다. (key는 변경되지 않아야 하는 것이 딕셔너리의 특징이기 때문)
c = {(1,2):'a'}
print(c[1,2])
#d = {[1,2],'a'} #오류 발생

#딕셔너리 주요 함수
d = {'a':1,'b':2,'c':3,'d':4}
print(d.keys()) #key들의 리스트로 이루어진 dict_keys 객채를 리턴함
for a in d.keys(): #for문에 활용 가능
    print(a)
print(list(d.keys())) #리스트로 변환 가능

print(d.values()) #value들의 리스트로 이루어진 dict_valus 객채를 리턴함
for a in d.values(): #for문에 활용 가능
    print(a)
print(list(d.values())) #리스트로 변환 가능

print(d.items()) #key, value 쌍을 튜플로 묶어놓은 리스트로 이루어진 dict_items 객체를 리턴함
for a in d.items(): #for문에 활용 가능
    print(a)
print(list(d.items())) #리스트로 변환 가능

b.clear()
print(b) #초기화

print(d.get('a')) #d['a']와 유사하지만 d['a']는 key가 없을 시 오류를 발생시키지만 get은 none을 리턴함
print(d.get('f')) #none리턴
print(d.get('f','no')) #get(a,default) a라는 key가 없을 시 default값 자체를 대신 리턴함

print('a' in d) # a in b -> b라는 딕셔너리에 'a'라는 키가 있으면 true 없으면 false 리턴
print('f' in d) #false 리턴