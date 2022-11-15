N = int(input())
A = list(map(int, input().split()))

for k in range(N-1):
    min_index = A[k:].index(min(A[k:]))+k
    A[k], A[min_index] = A[min_index], A[k]
    print(*A)
