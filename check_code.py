A, B = map(int, input().split())
S = input().strip()

if len(S) != A + B + 1:
    print("No")
    exit()

if S[A] != '-':
    print("No")
    exit()

for i in range(A + B + 1):
    if i != A:
        if not S[i].isdigit():
            print("No")
            exit()

print("Yes")
