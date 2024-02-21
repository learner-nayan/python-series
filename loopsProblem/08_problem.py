# METHOD ONE

# n = int(input("Enter a number: "))
#
# count = 0
#
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
#
# if count == 2:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")


# METHOD TWO

n = int(input("Enter a number: "))

is_prime = True

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print("Prime number:", is_prime)