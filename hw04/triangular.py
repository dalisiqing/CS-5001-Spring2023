import sys


def main(x):
    sum = 0
    for i in range(x + 1):
        sum += i
    print(' The "triangular number" of the input number is ' + str(sum))


main(int(sys.argv[1]))
