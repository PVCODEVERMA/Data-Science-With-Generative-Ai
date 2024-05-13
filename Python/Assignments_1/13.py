# Create a code to count the occurrencces of each element in list and return a dictionary with elements as keys and their counts as valuesḍ?

def count_elements(lst):
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict


my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 2, 2]
result = count_elements(my_list)
print(result)
