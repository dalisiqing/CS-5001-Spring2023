def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    # TODO: Fill in the rest of the necessary code here
    max_heart_rate = round((208 - 0.7 * age), 1)
    reserve = max_heart_rate - restHR
    # Calculate the min and max heart rate for the rang of each zone
    z1min = round((restHR + reserve * 0.5), 2)
    z1max = round((restHR + reserve * 0.6 - 0.01), 2)
    z2min = round((z1max + 0.01), 2)
    z2max = round((restHR + reserve * 0.7 - 0.01), 2)
    z3min = round((z2max + 0.01), 2)
    z3max = round((restHR + reserve * 0.8 - 0.01), 2)
    z4min = round((z3max + 0.01), 2)
    z4max = round((restHR + reserve * 0.93 - 0.01), 2)
    z5min = round((z4max + 0.01), 2)
    z5max = round((restHR + reserve), 2)

    print("Your heart rate reserve is: ", reserve, " bpm")
    print("Here is a breakdown of your training zones:")
    print("Zone 1: ", z1min, " to ", z1max, " bpm")
    print("Zone 2: ", z2min, " to ", z2max, " bpm")
    print("Zone 3: ", z3min, " to ", z3max, " bpm")
    print("Zone 4: ", z4min, " to ", z4max, " bpm")
    print("Zone 5: ", z5min, " to ", z5max, " bpm")

    print("=======================================")


main()
