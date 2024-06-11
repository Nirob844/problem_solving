N = input().strip()
reversed_N = str(int(N[::-1]))
print(reversed_N)
if N == N[::-1]:
    print("YES")
else:
    print("NO")
