import sys


def nose_cone(width):
    if width % 2 != 0:
        for row in range(1, width, 2):
            print(' '*((width - row)//2) + '*'*row)
    else:
        for row in range(2, width, 2):
            print(' '*((width - row)//2) + '*'*row)


def fuselage(width, length, striped=None):
    for i in range(length):
        if striped == 'striped':
            for j in range(width//2):
                print('_'*width)
            for j in range(width - width//2):
                print('X'*width)
        else:
            for j in range(width):
                print('X'*width)


def tail(width):
    if width % 2 != 0:
        if (width - width//2) % 2 != 0:
            for row in range(width//2 + 1, width, 2):
                print(' '*((width - row)//2) + '*'*row)
        else:
            for row in range(width//2, width, 2):
                print(' '*((width - row)//2) + '*'*row)
    else:
        if (width - width//2) % 2 != 0:
            for row in range(width//2 + 1, width, 2):
                print(' '*((width - row)//2) + '*'*row)
        else:
            for row in range(width//2, width, 2):
                print(' '*((width - row)//2) + '*'*row)
    print('*'*width)
    print('*'*width)


def main(x, y, z=None):
    nose_cone(x)
    fuselage(x, y, z)
    tail(x)


#  check for the length of sys.argv for the 3rd optional argument
if len(sys.argv) == 4:
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
else:
    main(int(sys.argv[1]), int(sys.argv[2]))
