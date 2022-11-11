#N本の紐
#L_{0} ~ L_{N-1}
#長さがA以上、B以下であるような紐の本数を答える（Q回の質問ごとに）


N = int(input())
L = list(map(int, input().split()))

# 上限:N=10^5以下の全てのひもの長さのパターンをリストとして用意して、
# 与えられたLの中身から任意の長さの紐が何本あるかを格納（ひもの長さの分布をリストとして作ってる

num_of_string = [0] * (10**5+1)
for l in L:
    num_of_string[l] += 1

# ひもの長さの累積分布をリストとして作成

acc = [0] * (10**5+1)
for idx, num in enumerate(num_of_string):
    if idx == 0:
        acc[idx] = num
    else:
        acc[idx] = acc[idx-1] + num

Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    res = acc[B] - acc[A-1]
    print(res)
    
    