
# tea_types = ("black", "green", "oolong")
# tea_types = ("black", "green", "oolong")
# tea_types
# ('black', 'green', 'oolong')
# tea_types[0]
# 'black'
# tea_types[0:2]
# ('black', 'green')
# tea_types[0] = "haha"
# Traceback (most recent call last):
#   File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# len(tea_types)
# 3
# more_tea = ("lemon", "milk", "masala")
# more_tea
# ('lemon', 'milk', 'masala')
# all_tea = tea_types + more_tea
# all_tea
# ('black', 'green', 'oolong', 'lemon', 'milk', 'masala')
# more_tea
# ('lemon', 'milk', 'masala')
# more_tea.append("lemon")
# Traceback (most recent call last):
#   File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'
# more_tea.insert(3, "lemon")
# Traceback (most recent call last):
#   File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'insert'
# more_tea = ("lemon", "milk", "masala", "lemon")
# print(more_tea)
# ('lemon', 'milk', 'masala', 'lemon')
# more_tea.count()
# Traceback (most recent call last):
#   File "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# TypeError: tuple.count() takes exactly one argument (0 given)
# more_tea.count("lemon")
# 2
# more_tea
# ('lemon', 'milk', 'masala', 'lemon')
# (Lemo, Mil, Masa, Lemo) = more_tea
# Lemo
# 'lemon'
# Mil
# 'milk'
# type
# <class 'type'>
