# FIRST WAY

# day = "wednesday"
# price_for_kids = 8
# price_for_adults = 12
# wednesday_disc = 2
#
# age = int(input("How old are you? "))
#
# if age < 18:
#     if day == "wednesday":
#         print("Ticket price is", price_for_kids - wednesday_disc)
#     else:
#         print("Ticket price is", price_for_kids)
# else:
#     if day == "wednesday":
#         print("Ticket price is", price_for_adults - wednesday_disc)
#     else:
#         print("Ticket price is", price_for_adults)

# SECOND WAY

# day = "wednesday"
# age = int(input("Enter your age: "))
# wednesday_disc = 2
#
# price = 12 if age >= 18 else 8
#
#
# if day == "wednesday":
#     print("Ticket price is $", price - wednesday_disc)
# else:
#     print("Ticket price is $", price)

# THIRD WAY

day = "wednesday"
age = int(input("Enter your age: "))
price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print("Your ticket price is", price)