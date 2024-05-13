# Write a code that takes a dictionary as input and returns a sorted version of it based on the values . you can choose whether to sort in ascending or descending order.


def sort_dict_by_values(input_dict, descending=True):
    """
    Sorts a dictionary by its values.

    Args:
        input_dict (dict): The input dictionary.
        descending (bool): If True, sorts in descending order; otherwise, sorts in ascending order.

    Returns:
        dict: A new dictionary sorted by values.
    """
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=descending)
    sorted_dict = dict(sorted_items)
    return sorted_dict


my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 3}
sorted_dict_desc = sort_dict_by_values(my_dict, descending=True)
sorted_dict_asc = sort_dict_by_values(my_dict, descending=False)

print("Sorted dictionary (descending order):", sorted_dict_desc)
print("Sorted dictionary (ascending order):", sorted_dict_asc)
