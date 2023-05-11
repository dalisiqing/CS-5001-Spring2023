from math import sqrt


def draw_circle(radius):
    x, y = radius, radius
    for i in range(2*radius):
        for j in range(2*radius):
            if sqrt((i - x)**2 + (j - y)**2) < radius:
                print(end='o')
            else:
                print(end=' ')
        print()


def main():
    draw_circle(int(input('Enter a number for the radius of a circle:')))


main()
