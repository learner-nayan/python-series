n = 10
sum_of_even_nums = 0

# for i in range(1, n+1):
for i in range(n+1):
    if i % 2 == 0:
        sum_of_even_nums += i

print(sum_of_even_nums)