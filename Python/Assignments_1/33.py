# Write a code  to access a value in a nested dictionary. the function should take the dicitionary and a list of keys as input and return the corresponding value . if any of the keys do not exist in the dictionary  the function should return none.

def get_nested_value(dictionary, keys):
    """
    Access a value in a nested dictionary based on a list of keys.

    Args:
        dictionary (dict): The nested dictionary.
        keys (list): List of keys representing the path to the desired value.

    Returns:
        Any: The corresponding value if found, or None if any key is missing.
    """
    current_dict = dictionary
    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            return None
    return current_dict


nested_dict = {
    "a": {
        "b": {
            "c": 42
        }
    }
}

keys_to_access = ["a", "b", "c"]
result = get_nested_value(nested_dict, keys_to_access)
print("Value:", result) 
