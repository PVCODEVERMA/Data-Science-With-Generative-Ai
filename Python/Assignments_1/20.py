# Write a code to shuffle a given list randomly without using any built-in shuffle function.

import random

def custom_shuffle(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        j = random.randint(0,i)
        lst[i], lst[j] = lst[j], lst[i]

my_list = [1,2,3,4,5]
custom_shuffle(my_list)
print("Shuffled list:",my_list)