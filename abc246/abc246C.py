N, K, X = map(int, input().split())
A = list(map(int, input().split()))
r = []
cost = sum(A)
c = K       # クーポンの枚数
f = sum(i // X for i in A)     # X円引ける回数
h = min(c, f)       # hにfとgの小さい方を代入
cost -= h * X       # 使用したクーポン分の値段を引く
for i in A:     # AをXで割った余り
    r.append(i % X)
d = sorted(r, reverse=True)     # cを降順にソート
c -= h      # 使用したクーポンの枚数を引く
cost -= sum(d[:c])      # 余ったクーポンを余りの大きい方から使用
print(cost)
