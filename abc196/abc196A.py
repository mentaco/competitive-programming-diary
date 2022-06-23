a, b = map(int, input().split())
c, d = map(int, input().split())
l = []
for x in range(a, b+1):
    for y in range(c, d+1):
        l.append(x-y)
print(max(l))
