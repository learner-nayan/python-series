numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0

for num in numbers:
    # print(num)
    if num > 0:
        positive_number_count += 1

print("No. of positive number is", positive_number_count)
