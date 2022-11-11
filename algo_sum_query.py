N = int(input())
A = list(map(int, input().split()))

# A_{0},...A_{N-1}
# l,rが与えられる（l<r）
# A_{l} + ... + A_{r-1} + A_{r}を計算する

# sum(A[l:r])を工夫して計算する

acc= [0]*(N+1)

for idx, a in enumerate(A):
    acc[idx+1] = acc[idx] + a

Q = int(input())

for _ in range(Q):
    l,r = map(int, input().split())
    sl = acc[l]
    sr = acc[r]
    print(sr-sl)