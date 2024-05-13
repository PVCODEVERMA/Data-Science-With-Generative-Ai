# Create a codde to find the union of two lists without duplicates.

def find_union(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    union = set1 | set2
    return list(union)

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

result = find_union(list1,list2)
print(result)
