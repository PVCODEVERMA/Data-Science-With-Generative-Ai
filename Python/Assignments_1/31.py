# write a code that takens a list of words  as input and returns a dicitionary where the keys are  unique words and the values are the frequences of those words in the input list.

def word_frequency(input_list):
    word_count = {}
    for word in input_list:
        
        cleaned_word = word.strip(".,!?").lower()
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    return word_count


input_words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
result = word_frequency(input_words)
print("Word frequencies:")
for word, count in result.items():
    print(f"{word}: {count}")
