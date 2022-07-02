K = int(input())
H = 21
while K >= 60:
    K -= 60
    H += 1
M = K
while H > 24:
    H -= 24
print("{:0=2}:{:0=2}".format(H, M))
