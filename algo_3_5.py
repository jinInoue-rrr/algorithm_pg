N = int(input())
A = list(map(int, input().split()))

# 配列の中身を順序逆にして出力
for i in range(N):
    print(A[N-1-i])