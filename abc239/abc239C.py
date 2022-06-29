x1, y1, x2, y2 = map(int, input().split())
p = [
    [1, 2], [2, 1],
    [2, -1], [1, -2],
    [-1, -2], [-2, -1],
    [-2, 1], [-1, 2]
    ]
f = False

for i in p:
    a = x1 + i[0]
    b = y1 + i[1]
    d1 = ((x1 - a)**2 + (y1 - b)**2)**(1/2)
    d2 = ((x2 - a)**2 + (y2 - b)**2)**(1/2)
    if d1 == d2 == 5**(1/2):
        f = True
        break

if f:
    print("Yes")
else:
    print("No")
