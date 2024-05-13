def count_words(input_string):
    words = input_string.split()
    return len(words)
input_string = "Hello, thes is a string."
word_count = count_words(input_string)
print(f"Number of words: {word_count}")