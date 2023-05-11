def christmas_tree(width):
    height = (width - 1)//2 + 1
    row = 0
    for row in range(height):
        # Print the top of tree
        if row == 0:
            print(' '*((width - 1)//2) + '*')
        # print the bottom of tree
        elif row == height - 1:
            print('/' + '_'*(width - 2) + '\\')
        # print the lines between the top and bottom of the tree
        else:
            print(' '*((width - 1)//2 - row) + '/' + ' '*(row*2 - 1) + '\\')
        row += 1


def main():
    x = 0
    while x % 2 == 0 or x < 3:
        x = int(input('Please enter an odd integer greater '
                      'than 3 for the width of the base of the tree:'))
    christmas_tree(x)


main()
