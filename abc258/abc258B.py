from tkinter import W


N = int(input())
m = []
for _ in range(N):
    num = input()
    m.append(list(map(int, list(num))))

a = max(list(map(lambda x: max(x), m)))
s = str(a)

for i in m:
    if max(i) == a:
        l = m.index(i)
        r = i.index(a)

x = l
y = r
lis = [[x, y]]

for i in range(N-1):
    p = (x-1) % N
    q = (y-1) % N
    h = 0
    c = 1
    for j in range(9):
        if not((p == x and q == y) or [p, q] in lis):
            if h < m[p][q]:
                h = m[p][q]
                v = p
                w = q
            
        if c % 3 == 0:
            q = (q-2) % N
            p = (p+1) % N
        else:
            q = (q+1) % N
        c += 1

    s += str(h)
    x = v
    y = w
    lis.append([x, y])

print(s)
# 結果：RE
