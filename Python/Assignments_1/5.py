
import re


def  find_all_accourrence(string, sub):
    return[m.start() for m in re.finditer(re.escape(sub), string)]
input_string = "test test test"
substring = "test"
occurrences = find_all_accourrence(input_string, substring)

print(occurrences)

