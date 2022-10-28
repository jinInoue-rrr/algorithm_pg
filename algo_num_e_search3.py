N = int(input())
flag2 = False
if N >= 2:
    flag2 = True

flagn = True

for i in range(2, N):
    if N % i == 0:
        flagn = False
        
if flag2 == True and flagn == True:
    print("Yes")
else:
    print("No")



