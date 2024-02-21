# def print_kwargs(name, surname):
#     print('Name:', name, 'Surname:', surname)
#
#
# print_kwargs(name='Nayan', surname='Khanal')
# print_kwargs(surname='Khanal', name='Nayan')
# print_kwargs(name='Nayan')

# SO

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_kwargs(name='Nayan', surname='Khanal')
print_kwargs(surname='Khanal', name='Nayan')
print_kwargs(name='Nayan')