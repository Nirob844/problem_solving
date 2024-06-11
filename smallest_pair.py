T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    
    min_sum_value = float('inf')
    
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            sum_value = A[i - 1] + A[j - 1] + (j - i)
            if sum_value < min_sum_value:
                min_sum_value = sum_value
    
    print(min_sum_value)
