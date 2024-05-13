
def characters(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

input_string = "aadsds"
print(characters(input_string))