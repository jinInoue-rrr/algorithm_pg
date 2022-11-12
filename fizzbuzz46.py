N = int(input())
for i in range(1, N+1):
    if i%4 == 0 and i%6 == 0:
        print("FizzBuzz")
    else:
        if i%4 == 0:
            print("Fizz")
        elif i%6 == 0:
            print("Buzz")
        else:
            print(i)