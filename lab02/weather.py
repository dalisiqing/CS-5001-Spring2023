def dif(highest,lowest):
    difference = highest - lowest
    print ("The difference between the highest and the lowest temperature values predicted for the 10 day forecast is ", difference)

def avg(a,b,c,d,e,f,g,h,i,j):
    average = (a+b+c+d+e+f+g+h+i+j)//10
    print("The average temperature at noon predicted for the 10 day forecast is ", average)

def highest(temperature):
    degreesC = round(5/9*(temperature - 32))
    print("The highest temperature predicted for the 10 day forecast is " , degreesC , " in Celsius.")

print("Today is January 24, 2023.")
dif(48,26)
avg(43,47,44,46,44,38,34,35,37,39)
highest(48)

