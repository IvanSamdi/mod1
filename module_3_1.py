calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_conteins(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_conteins('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_conteins('cycle', ['recycle', 'cyclic']))
print(calls)