# Write a code to reverse a list in-place without using any built-in reverse functions.

def reverse_list_in_place(lst):
    left, right  = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -+ 1

my_list = [1,2,3,4,5]
reverse_list_in_place(my_list)
print(my_list)