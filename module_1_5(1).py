immutable_var = tuple([1, 2, 'a', 'b'])
print(immutable_var)
print(type(immutable_var))
# immutable_var [2]= 3
# print(immutable_var) #невозможно т.к кортеж относится к неизменяемым типам данных и не поддерживает обращение к элементам
mutable_list = [1, 2, 'a', 'b']
print(mutable_list)
mutable_list[2] = 3
print(mutable_list)
