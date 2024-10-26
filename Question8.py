def keys_with_values_greater_than(d, n):
    return [key for key, value in d.items() if value > n]

my_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_with_values_greater_than(my_dict, n)
print(result)
