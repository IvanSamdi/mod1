# Функция с параметрами по умолчанию
def print_params(a=1, b='stroka', c=True):
    print(a, b, c)


print_params()
print_params(5, 'строка', False)
print_params(32.0, 'aloha!')
print_params(b=25)
print_params(a='stroka')
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [123, 'shalom', True]
values_dict = {'a': 33, 'b': 'good_day', 'c': False}
print_params(**values_dict)
print_params(*values_list)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'STROKA']
print_params(*values_list_2, 42)
