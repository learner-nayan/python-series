marks = int(input("Enter marks: "))

if marks < 60:
    print("F")
elif marks < 70:
    print("D")
elif marks < 80:
    print("C")
elif marks < 90:
    print("B")
elif marks < 100:
    print("A")
else:
    print("Please enter a valid mark")
    exit()

