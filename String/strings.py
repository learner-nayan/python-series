# string basic
str = "nayan"
print(str)

# string index
str2 = "khanal"
print(str2[0])

print(str2[0:4])
print(str2[0:6:2])

# uppercaser lowercase
str3 = "heLLo everyone"
print(str3)
print(str3.upper())
print(str3.lower())

# stripping >>> removes extra spaces
new_string = "     nayan khanal is a brilliant student   "
print(new_string.strip())

# replace
new_string2 = "hello everyone, my name is nayan"
print(new_string2)
print(new_string2.replace("hello", "hi"))

# splitting
commalist = "ram, shyam, hari"
print(commalist)
print(commalist.split(", "))

# doing something more with splitting
# commalist_managed = commalist.split(", ")
# for names in commalist_managed:
#     print(names.upper())

# finding
my_string = "bhanu bhakta acharya"
print(my_string.find("bhanu"))
print(my_string.find("bhakta"))

# counting
my_string2 = "Elon Musk Musk"
print(my_string2.count("Elon"))
print(my_string2.count("Musk"))

# putting string value in an another string
coffee = "black"
quantity = 2
order = "I ordered {} cups of {} coffee"
print(order.format(quantity,coffee))

# joining
mero_string = ["nayan", "don", "dada"]
print("".join(mero_string))
print(", ".join(mero_string))

# length
hello_string = "Hello hello hi hello"
print(len(hello_string))

for letter in hello_string:
    print(letter)

# back slash and back slash problem in strong
chiya = "He said, \"Nayan is a brilliant student.\""
print(chiya)

# raw string
chiya2 = r"C:\\user\nayan"
print(chiya2)

# search
last_str = "My name is Nothing"

print("Nothing" in last_str)      #true
print("nothing" in last_str)      #false