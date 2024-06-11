N = int(input())
A = list(map(int, input().split()))

min_value = min(A)
max_value = max(A)
min_index = A.index(min_value)
max_index = A.index(max_value)

A[min_index], A[max_index] = A[max_index], A[min_index]

print(" ".join(map(str, A)))
