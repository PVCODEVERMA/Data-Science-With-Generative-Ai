# Implement a code to find remove duplicates from a list while preserving the original order of elements.


def remove_duplicates(original_list):
    unique_elements = {}
    result = []

    for item in original_list:
        if item not in unique_elements:
            unique_elements[item] = True
            result.append(item)
    return result

my_list = [1,2,3,2,4,1,5,3]
unique_list = remove_duplicates(my_list)
print(unique_list)