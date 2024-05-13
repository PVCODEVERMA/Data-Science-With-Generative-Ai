def anagrams(str1,str2):
    str1 = str1.replace("","").lower()
    str1 = str2.replace("","").lower()

    return sorted(str1) ==sorted(str2)

string1 = input("Enter the fiast string:")
string2 = input("Enter the fiast string:")


if anagrams(string1, string2):
    print("The string are anagrams of each other.")
else:
    print("The strings are not anagrams.")