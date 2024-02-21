
# name_surname = {"nayan": "khanal", "ram": "bhattarai", "hari": "baral"}
# name_surname
# {'nayan': 'khanal', 'ram': 'bhattarai', 'hari': 'baral'}
# for name in name_surname:
#     print(name, name_surname[name])
#
# nayan
# khanal
# ram
# bhattarai
# hari
# baral
# name_surname["nayan"]
# Traceback(most
# recent
# call
# last):
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/code.py", line
# 63, in runsource
# code = self.compile(source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 153, in __call__
# return _maybe_compile(self.compiler, source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 73, in _maybe_compile
# return compiler(source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 118, in __call__
# codeob = compile(source, filename, symbol, self.flags, True)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "<input>", line
# 1
# name_surname["nayan"]
# IndentationError: unexpected
# indent
# name_surname[nayan]
# Traceback(most
# recent
# call
# last):
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/code.py", line
# 63, in runsource
# code = self.compile(source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 153, in __call__
# return _maybe_compile(self.compiler, source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 73, in _maybe_compile
# return compiler(source, filename, symbol)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/codeop.py", line
# 118, in __call__
# codeob = compile(source, filename, symbol, self.flags, True)
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# File
# "<input>", line
# 1
# name_surname[nayan]
# IndentationError: unexpected
# indent
# print("hello")
# hello
# print(name_surname)
# {'nayan': 'khanal', 'ram': 'bhattarai', 'hari': 'baral'}
# print(name_surname["nayan"])
# khanal
# for key, values in name_surname.items():
#     print(key, values)
#
# nayan
# khanal
# ram
# bhattarai
# hari
# baral
# if "nayan" in name_surname:
#     print("yes")
#
# yes
# name_surname["name"] = "surname"
# print(name_surname)
# {'nayan': 'khanal', 'ram': 'bhattarai', 'hari': 'baral', 'name': 'surname'}
# name_surname.pop("nayan")
# 'khanal'
# print(name_surname)
# {'ram': 'bhattarai', 'hari': 'baral', 'name': 'surname'}
# name_surname.popitem()
# ('name', 'surname')
# print(name_surname)
# {'ram': 'bhattarai', 'hari': 'baral'}
# del name_surname["ram"]
# print(name_surname)
# {'hari': 'baral'}
# name_surname_new = name_surname.copy()
# name_surname["nayan"] = "khanal"
# print(name_surname)
# {'hari': 'baral', 'nayan': 'khanal'}
# print(name_surname_new)
# {'hari': 'baral'}
# tea = {}
# tea_shop = {
#     chiya: {"masala": "mitho", "sadha": "ok"},
#     tea: {"milk": "great", "Lemon": "wow"}
# }
# Traceback(most
# recent
# call
# last):
# File
# "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line
# 364, in runcode
# coro = func()
# ^ ^ ^ ^ ^ ^
# File
# "<input>", line
# 2, in < module >
# NameError: name
# 'chiya' is not defined
# tea_shop = {
#     "chiya": {"masala": "mitho", "sadha": "ok"},
#     "tea": {"milk": "great", "Lemon": "wow"}
# }
# print(tea_shop)
# {'chiya': {'masala': 'mitho', 'sadha': 'ok'}, 'tea': {'milk': 'great', 'Lemon': 'wow'}}
# print(tea_shop["chiya"])
# {'masala': 'mitho', 'sadha': 'ok'}
# print(tea_shop.get("chiya"))
# {'masala': 'mitho', 'sadha': 'ok'}
# print(tea_shop["chiya"]["masala"])
# mitho
# squared_num = [x ** 2 for x in range(10)]
# print(squared_num)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# squared_num2 = {x: x ** 2 for x in range(10)}
# print(squared_num)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(squared_num2)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# squared_num2.clear()
# print(squared_num2)
# {}
# coffee = ["latte", "capaccino", "Sikandar"]
# print(coffee)
# ['latte', 'capaccino', 'Sikandar']
# default_value = "mitho"
# coffee_dict = dict.fromkeys(keys, default_value)
# Traceback(most
# recent
# call
# last):
# File
# "/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevconsole.py", line
# 364, in runcode
# coro = func()
# ^ ^ ^ ^ ^ ^
# File
# "<input>", line
# 1, in < module >
# NameError: name
# 'keys' is not defined.Did
# you
# mean: 'key'?
# coffee_dict = dict.fromkeys(key, default_value)
# print(coffee_dict)
# {'h': 'mitho', 'a': 'mitho', 'r': 'mitho', 'i': 'mitho'}
# coffee_dict = dict.fromkeys(coffee, default_value)
# print(coffee_dict)
# {'latte': 'mitho', 'capaccino': 'mitho', 'Sikandar': 'mitho'}


