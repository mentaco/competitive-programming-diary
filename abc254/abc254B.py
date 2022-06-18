n = int(input())
dp = [[0] * (i+1) for i in range(n)]

for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
for i in range(n):
    print(*dp[i])
