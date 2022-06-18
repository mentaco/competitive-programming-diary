N = int(input())
s = []
for i in range(N):
    LR = list(map(int, input().split()))
    s.append(LR)
s.sort()
k = 0
while 1:
    if s[k][1] >= s[k+1][0]:
        l = s[k][0]
        r = max(s[k][1], s[k+1][1])
        del s[k]
        del s[k]
        s.insert(k, [l, r])
    else:
        k += 1

    if k == len(s)-1 or len(s) == 1:
        break
    
for i in s:
    print(*i)

# 結果：RE
