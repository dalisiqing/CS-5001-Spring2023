import math
def main():
    print('Please enter value for x1:')
    x1 = float(input())
    print('Please enter value for y1:')
    y1 = float(input())
    print('Please enter value for x2:')
    x2 = float(input())
    print('Please enter value for x2:')
    y2 = float(input())
    Euclidean_distance = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
    print("The Euclidean distance between the two points is ", Euclidean_distance)
    
main()