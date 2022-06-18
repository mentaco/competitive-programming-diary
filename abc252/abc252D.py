from math import comb
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
count_elem = Counter(A)
x = comb(N, 3)

for i in count_elem.values():
    x -= comb(i, 2) * (N - i)
    x -= comb(i, 3)

print(x)
