# write a code to perform basic string compression using the counts of repeated characters characters in python





def compress_string(s):
    compressed = ""
    count = 1

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1

    return compressed if len(compressed) < len(s) else s

input_string = "asasdsads"
compressed_result = compress_string(input_string)
print("compressed string:", compressed_result)