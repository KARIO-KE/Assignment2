def reverse_strings(strings):
    reversed_list = []
    for string in strings:
        reversed_list.append(string[::-1])
    return reversed_list
strings = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(strings))