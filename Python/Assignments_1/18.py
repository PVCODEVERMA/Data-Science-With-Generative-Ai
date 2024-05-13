# Implement a code to find the intersection of two given lists.

def intersection(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1 & set2
    return list(intersection)


list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
result = intersection(list1,list2)
print("Intersection:",result)

