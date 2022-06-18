N = int(input())
A = list(map(int, input().split()))
P = 0

for i in range(1, N):
    for j in range(i):
        A[j] += A[i]

for i in A:
    if i > 3:
        P += 1

print(P)
