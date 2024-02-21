# METHOD ONE

# items = ["apple", "banana", "orange", "apple", "mango"]
#
# for item in items:
#     if items.count(item) > 1:
#         print(item)
#         break
#


# SECOND METHOD

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
    else:
        unique_items.add(item)

