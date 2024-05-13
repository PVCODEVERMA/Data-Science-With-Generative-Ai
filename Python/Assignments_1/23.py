# write a code to concatenate two tuples. the function should take two tuples as input and return a new  tuple containing elements from both input tuples.

def concatenate_tuples(tuple1,tuple2):
    result_tuple = tuple1 + tuple2
    return result_tuple

tuple1 = (1,2,3)
tuple2 = (4,5,6)

concatenated_tuple = concatenate_tuples(tuple1,tuple2)

print("Concatenated tuple:",concatenated_tuple)