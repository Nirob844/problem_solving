A, B = map(int, input().split())

lucky_numbers = []

for num in range(A, B + 1):
    num_str = str(num)
    
    is_lucky = True
    
    for digit in num_str:
        if digit != '4' and digit != '7':
            is_lucky = False
            break
    
    if is_lucky:
        lucky_numbers.append(num_str)

if lucky_numbers:
    print(" ".join(lucky_numbers))
else:
    print(-1)
