n,m = map(int, input().split())
not_listen = set([input() for _ in range(n)]) #O(n)
not_see = set([input() for _ in range(m)]) #O(n)
not_listen_see = sorted(list(not_listen & not_see))
print(len(not_listen_see))
for i in not_listen_see:
    print(i)