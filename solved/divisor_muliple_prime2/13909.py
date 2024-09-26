n = int(input())
window = [1]*(n+1)
for i in range(2,n+1):
    for j in range(1,n//i+1):
        