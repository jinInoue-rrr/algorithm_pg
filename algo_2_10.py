S = input()
N, M = map(int, input().split())
s_list = list(S)
tmp_n = s_list[N-1]
tmp_m = s_list[M-1]
s_list[N-1] = tmp_m
s_list[M-1] = tmp_n
print("".join(s_list))