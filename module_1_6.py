my_dict = {'Natasha': 1978, 'Sveta': 1980, 'Masha': 1983}
print(my_dict)
my_dict['Lory'] = 1987
print(my_dict['Masha'])
print(my_dict['Lory'])
my_dict.update({'Ivan': 1977, 'Marina': 1989})
a = my_dict.pop('Sveta')
print(my_dict.get('Sveta'))
print(a)
print(my_dict)
# работа с множествами
my_set = {1, 2, 3, 4, 'Masha', 'Lory', 4, 3, 2, 1, 5}
my_set.add((6, 7))
my_set.discard('Masha')
print(my_set)
