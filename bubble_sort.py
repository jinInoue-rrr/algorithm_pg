N = int(input())
A = list(map(int, input().split()))

#並べ替えのループをN回
for _ in range(N):
    flag = False
    for i in range(N-1):
        if A[i] > A[i+1]:
            flag = True
            A[i], A[i+1] = A[i+1], A[i]#交換
    if flag:
        print(*A)
    else:
        break





