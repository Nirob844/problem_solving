N = int(input())

fib1 = 0
fib2 = 1

if N == 1:
    print(fib1)
elif N == 2:
    print(fib2)
else:
    for i in range(3, N + 1):
        fib_next = fib1 + fib2
        fib1 = fib2
        fib2 = fib_next
    print(fib2)
