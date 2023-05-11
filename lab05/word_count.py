import string
import re


def main():
    # Try blocks to handle possible failures to open files
    try:
        filename = input('Enter the file name: ')
        f = open(filename, "r", encoding="utf-8")
        s = open(filename, "r", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"Can't open {filename}")
        return
    # Try to read each line of the file
    words_count = 0
    non_whitespace_count = 0

    for line in f:
        words_count += len(line.split())
        non_whitespace_count += len(line.replace(' ', '').replace('\n', '')
                                    .replace('\t', '').replace('\b', '')
                                    .replace('\f', '').replace('\r', ''))
    contents = s.read()
    alphanumer_count = len(re.findall(r'\w', contents))

    print(f'Words: {words_count}\nCharacters: {non_whitespace_count}\
          \nLetters & numbers: {alphanumer_count}')


main()
