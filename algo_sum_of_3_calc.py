# 計算量の工夫
# 正の整数N, Mが与えられる
# x,y,zはそれぞれ1以上N以下の整数
# x,y,zの総和はM以下である

# 2つの条件を満たす正の整数の組の数を見つける

# 3つのloopを回すとO(N^3)となり、N = 2000の制約の元では、N^3 <= 2000^3で実行時間に間に合わない問題が生じる(TLE)

# 制約を利用して、xとyのみを動かすことにして計算量を減らす
# z <= min(N, M-x-y)を使う

N, M = map(int, input().split())

ans = 0

for x in range(1, N+1):
    for y in range(1, N+1)
        max_z = min(N, M-x-y)
        if max_z <= 0:
            continue
        ans += max_z#(x,y)の組について、1<= z <= max_zの数だけ組が存在するからその分ケースを足し上げる

print(ans)








