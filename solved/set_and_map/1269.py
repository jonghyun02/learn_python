n,m = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
s = A-B|B-A
print(len(s))