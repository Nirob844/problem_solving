N = int(input())

even_found = False

for i in range(2, N + 1, 2):
    print(i)
    even_found = True

if not even_found:
    print(-1)
