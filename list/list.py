#list
teas = ["Milk", "Masala", "Black", "Lemon"]
print(teas)

#replacing values

teas[1] = "Removed"
print(teas)

teas[1] = "Masala"
print(teas)

teas[1:2] = []
print(teas)

teas.insert(1,"Hello")
print(teas)

# comprehensive list
square_nums = [x**2 for x in range(10)]
print(square_nums)

cube_nums = [y**3 for y in range(10)]
print(cube_nums)

#copying list in another list variable >>>>>>just pointing the same memory location/address by another variable too
square_nums_copy_same_address = square_nums
cube_nums_copy_real_new = cube_nums.copy()

square_nums_copy_same_address.pop()
print(square_nums_copy_same_address)
print(square_nums)     # this also changed because of same memory location pointed by two different variables

cube_nums_copy_real_new.pop()
print(cube_nums_copy_real_new)
print(cube_nums)       # this did not change because we created the new copy on different memory location with .copy()



# we have many functions for list like:
#     list_name.append("string_here")
#     list_name.remove("string_here")