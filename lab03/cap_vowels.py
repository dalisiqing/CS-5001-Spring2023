def capitalize_vowel(string_of_input):
    result = ""
    for c in string_of_input:
        if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
             or c == 'I' or c == 'i' or c == 'O' or c == 'o':
            result += c.upper()
        else:
            result += c.lower()
    print(result)


capitalize_vowel(input('Please enter a string: '))
