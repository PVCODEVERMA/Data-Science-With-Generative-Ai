# wrire a code  that takes two tuples as input abd returns and new tuple containing elements that  are common to both input tuples.

def find_elements(tuple1,tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)

    common_element = set1 & set2
    result_tuple = tuple(common_element)

    return result_tuple
tuple1 = (1,2,3,4,5)
tuple2 = (3,4,5,6,7)

result = find_elements(tuple1,tuple2)
print("common elements:", result)