def magic_square(lst):
    print('Enter a magic number:')
    # Create a list for the input of user for the
    # three separate lines of number
    line = []
    for i in range(3):
        line.append(list(map(int, input())))

    # Get the sums of the sum of any 3 digits horizontally
    sums = lst
    for x in line:
        sum = 0
        for y in x:
            sum += y
        sums.append(sum)
    # Get the sums of the sum of any 3 digits vertically
    for i in range(3):
        sum = 0
        for x in line:
            sum += x[i]
        sums.append(sum)
    # Get the sums of the sum of any 3 digits diagonally
    sum = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                sum += line[i][j]
    sums.append(sum)
    sum = 0
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            if i == j:
                sum += line[i][j]
    sums.append(sum)


def checkList(lst):
    member = lst[0]
    result = True
    # Comparing each member in sums
    for x in lst:
        if member != x:
            result = False
            break
    if result:
        print("This is a magic square!")
    else:
        print("Not a magic square!")


def main():
    # Create a list for sums of the
    # input values in all 8 directions
    magic_sums = []
    magic_square(magic_sums)
    checkList(magic_sums)


main()
