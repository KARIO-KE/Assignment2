def tuples_to_dict(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict
tuples_input = [("apple", 5), ("banana", 3), ("orange", 4)]
result = tuples_to_dict(tuples_input)
print(result)
