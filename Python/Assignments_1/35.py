# Write a code that inverts a dictionary swapping keys and values.Ensure that inverted dictionary correctly handles cases where multiple keys have the same value by storting the keys as a list in the inverted dictionary.

def invert_dictionary(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict


my_dict = {"apple": 5, "banana": 2, "cherry": 5, "date": 2}
inverted_result = invert_dictionary(my_dict)

print("Inverted dictionary:")
for value, keys in inverted_result.items():
    print(f"{value}: {keys}")
