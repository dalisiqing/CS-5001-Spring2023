import math
def main():
    degree = float(input("Enter an angle: "))
    angle = degree*(math.pi)/180
    cosine = math.cos(angle)
    sine = math.sin(angle)
    print ("The cosine of ", degree, " is ", cosine)
    print ("The sine of ", degree, " is ", sine)

main()