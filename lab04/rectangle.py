def rectangle():
    symbol = input('Please input a character as a symbol for the rectangle:')
    width = int(input('Please input a integer as the width of the ractangle:'))
    height = int(input('Please input a integer as '
                       'the height of the ractangle:'))
    if width < 2 or height < 2:
        print('The value is too small')
        print()
    else:
        for i in range(height):
            if i == 0 or i == height - 1:
                print(symbol*width)
            else:
                print(symbol + ' '*(width - 2) + symbol)


def main():
    rectangle()


main()
