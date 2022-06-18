n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [[] for _ in range(k)]
c = []

for i in range(n):
    b[i%k].append(a[i])

for i in b:
    i.sort()

for i in range(n):
    c.append(b[i%k][i//k])

if sorted(c) == c:
    print("Yes")
else:
    print("No")
