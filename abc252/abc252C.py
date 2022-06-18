N = int(input())
S = [input() for _ in range(N)]
num = [[] for _ in range(10)]
count = [[0]*10 for _ in range(10)]
time = [0 for _ in range(10)]

for i in S:
    for j in range(10):
        num[int(i[j])].append(j)
        count[int(i[j])][j] += 1

for i in range(10):
    for j in range(N):
        num[i][j] += (count[i][num[i][j]] - 1) * 10

for i in range(10):
    time[i] = max(num[i])

print(min(time))
