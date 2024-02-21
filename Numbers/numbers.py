# start
x = 2
y = 3

sums = x + y

print(x)
print(y)
print(sums)

# int float change
print(int(3.5))
print(float(5))

# power
print(x ** 2)

# repr , print , str
print("nayan-print")
print(str("nayan-str"))
print(repr("nayan-repr"))

# import math

import math
print(math.floor(3.5))
print(math.trunc(2.89))
print(oct(62))
print(int('62',8))
print(hex(44))

# import random
import random
arr = ['nayan','khanal','jhapa']
print(random.choice(arr))

brr = [1,2,3,4,5,6,7,8,9]
print(random.choice(brr))

print(random.randint(1,9))


# import decimal
# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
# >>>>>>>>>>>>>>>>>>>>>>>This did not work<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# fractions
# from fractions import Fraction
# my_fraction = Fraction(3,2)
# print(my_fraction)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>This did not work<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# sets
set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6,7}
print(set1)
print(set2)
print(set1 and set2)
print(set1 or set2)