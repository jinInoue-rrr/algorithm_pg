N = int(input())
A = [""] * N
for i in range(N):
    A[i] = input()
ans = 0
for item in A:
    ans += len(item)
print(ans)