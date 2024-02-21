username = "nayan"


def func():
    username = "chai"
    print(username)


print(username)
func()


x = 10
def nayan(num):
    def actual(x):
        return x ** num
    return actual

f = nayan(2)
g = nayan(3)

print(f(3))
print(g(3))


