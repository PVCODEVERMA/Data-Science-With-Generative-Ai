# write a code that takes a tuple and an element as input . the function  should return the count  of occurrences of the given element in the tuple.

def count_occurrences(input_tuple,target_element):
    return input_tuple.count(target_element)
my_tuple = (1,2,3,2,4,2,5)
element_to_count = 2
result = count_occurrences(my_tuple,element_to_count)
print(f"Occurrence of {element_to_count} in the tuple: {result}")