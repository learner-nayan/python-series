# FIRST METHOD

# password = input("Enter your password: ")
#
# if len(password) < 6:
#     print("Your password is weak")
# elif len(password) < 10:
#     print("Your password is medium")
# else:
#     print("Your password is strong")


# SECOND METHOD

password = input("Enter your password: ")

if len(password) < 6:
    strength = "weak"
elif len(password) < 10:
    strength = "medium"
else:
    strength = "strong"

print("Your password is", strength)