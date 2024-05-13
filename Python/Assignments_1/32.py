# write a code that takes two dicitionaries as input and merges them into a single dicitionary.if  there are common keys the values should be added togeter.

def merge_dicitionaries(dict1,dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}
result = merge_dicitionaries(dict1,dict2)
print("Merged dictionary:", result)