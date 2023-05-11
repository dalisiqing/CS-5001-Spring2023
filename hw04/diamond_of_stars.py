import sys


def main(height):
    if height % 2 != 0:
        width = height
        # Increment range for top half triangle
        for row in range(1, (height - 1)//2 + 1):
            print(' '*((width - (2*row - 1))//2) + '*' * (2*row - 1))
        # Center line
        print('*' * width)
        # Decrement range for bottom half triangle
        for row in range((height - 1)//2, 0, -1):
            print(' '*((width - (2*row - 1))//2) + '*' * (2*row - 1))
    else:
        width = height - 1
        # Increment range for top half triangle
        for row in range(1, (height - 2)//2 + 1):
            print(' '*((width - (2*row - 1))//2) + '*' * (2*row - 1))
        # Center line
        print('*' * width)
        print('*' * width)
        # Decrement range for bottom half triangle
        for row in range((height - 2)//2, 0, -1):
            print(' '*((width - (2*row - 1))//2) + '*' * (2*row - 1))


main(int(sys.argv[1]))
