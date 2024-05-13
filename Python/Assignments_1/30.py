# Develop a code that prompts the user to input two sets of strings. then print the symmetric defference of thesr two sets.

def input_set():
    try:
        user_input = input("Enter a set of strings separated by commas: ")
        string_list = [s.strip() for s in user_input.split(",")]
        return set(string_list)
    except ValueError:
        print("Invalid input. Please enter strings separated by commas.")
        return input_set()

set1 = input_set()
set2 = input_set()


symmetric_difference = set1 ^ set2

print("Symmetric difference of the two sets:", symmetric_difference)
