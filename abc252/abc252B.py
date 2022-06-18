N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
flag = 0

for i in B:
    if A[i-1] == max(A):
        flag = 1
        break

if flag == 1:
    print("Yes")
else:
    print("No")
