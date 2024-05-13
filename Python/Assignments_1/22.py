# Create a code that prompts the user to enter two sets of integers separated by commas. then , print the  intersection of these two sets.

def input_set():
    try:
        user_input = input("Enter a set of integers separated by commas: ")
        integer_list = [int(x) for x in user_input.split(",")]
        return set(integer_list)
    except ValueError:
        print("Invalid input. Please enter integers separated by commas.")
        return input_set()


set1 = input_set()
set2 = input_set()


intersection = set1 & set2

print("Intersection of the two sets:", intersection)
