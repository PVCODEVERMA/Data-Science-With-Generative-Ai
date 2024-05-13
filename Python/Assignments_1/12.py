# implement a code  to find the second largest number in a given list of integers in python

def find_second_largest(numbers):
   sublist = [x for x in numbers if x <max(numbers)]
   return max(sublist)
my_list = [10,20,30,4,54,99]

result = find_second_largest(my_list)
print("Second largest number is:", result)