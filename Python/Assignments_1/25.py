# Create a code that takes a tuple and two integers as inputs. the function should return a new tuple containing elements from the original tuple within the specified range of indices.

def extract_subtuple(original_tuple,start_index,end_index):
    if start_index < 0 or end_index >=len(original_tuple) or start_index > end_index:
        return None
    subtuple = original_tuple[start_index:end_index +1]
    return tuple(subtuple)

my_tuple = (1,2,3,4,5,6,7)
start = 2
end = 5
result = extract_subtuple(my_tuple,start,end)
print("Subtuple:", result)