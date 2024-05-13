# Develop a code that prompts the user to input two sets os strings. then print the elements that are present in the first set but not in the second set

def input_set():
    try:
        user_input = input("Enter a set of strings separate by commas:")
        string_list = [s.strip() for s in user_input.split(",")]
        return set(string_list)
    except ValueError:
        print("Invalid input.Please enter strings separated by commas.")
        return input_set()
set1 = input_set()
set2 = input_set()

defference = set2 - set2

print(defference)