# Create a code to check if a given list is sorted(either in ascending order) or not.

def  sorted(lst):
    for i in range(len(lst) -1):
        if lst[i] > lst[i + 1]:
            return False
        return True
    
my_list = [1,3,5,7,9]

if sorted(my_list):
    print("The list is sorted in ascending order")
else:
    print("The list is not sorted in ascending order.")