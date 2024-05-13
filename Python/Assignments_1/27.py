# Develop a code that  takes a tuple of integers as input. the function should return the maximum and minimum values from the tuple using tuple unpacking.


def find_max_min_values(input_tuple):
    *rest,last = input_tuple
    max_value = max(rest)
    min_value = min(rest)
    return max_value, min_value
my_tuple = (10,5,8,3,12,7)
max_val,min_val = find_max_min_values(my_tuple)
print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
