# write a code that prompts the user to input two sets of characters.  then print the union of  these  two sets.

def input_set():
    try:
        user_input = input("Enter a set of sharacters (separated by commas): ")
        char_list = [c.strip() for c in user_input.split(",")]
        return set(char_list)
    except ValueError:
        print("Invalid input .please enter characters separated.")
        return input_set()
    
set1 = input_set()
set2 = input_set()

union = set1 | set2

print("Union of the two sets:", union)