import string


def main():
    # Try blocks to handle possible failures to open files
    try:
        filename = input('Please enter the file name: ')
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError as e:
        print(f"Unable to open {filename}")
        return

    # Initialize all the result counts
    duration_mins = 0
    watts = 0
    pump_watts1min = 1000
    running_mins = 0
    gallons = 0
    reach1 = -1
    reach2 = -1
    bar_value = 150
    long_run_start = []
    long_run_mins = []
    long_run_start_moment = 0
    long_run_stop_moment = 0
    long_run_length = 0
    long_run_status = False

    # Read each line of the file
    # Updated all the counts initialized before
    # Record the unmber of gallons when it reachs each level need to report
    for line in f:
        watts += int(line.rstrip())
        duration_mins += 1
        running_mins = round(watts/pump_watts1min, 3)
        gallons = round(running_mins*2, 3)

        if gallons >= 5 and reach1 == -1:
            reach1 = duration_mins
        elif gallons >= 100 and reach2 == -1:
            reach2 = duration_mins

        # start long run count
        if int(line.rstrip()) > bar_value:
            long_run_stop_moment = duration_mins
            long_run_length = long_run_stop_moment - long_run_start_moment
            # reocrd the start point by adjustment
            if long_run_length >= 120 and not long_run_status:
                long_run_start.append(duration_mins - 119)
                long_run_status = True

        # stop long run count
        # reocrd the stop point
        else:
            if long_run_length >= 120:
                long_run_mins.append(round(long_run_length))
            # clear the long run count and status
            long_run_length = 0
            long_run_start_moment = duration_mins
            long_run_status = False

    # Calculation for the result counts
    duration_hrs = round(duration_mins/60, 1)
    duration_days = round(duration_hrs/24, 3)
    gallons_per_day = round(round(gallons)/(duration_hrs/24), 1)
    kwhs = round(watts/60000, 3)

    # Print the result counts and the report
    print(f'Data covers a total of {duration_hrs} hours')
    print('(That\'s {0} days)'.format(duration_days))
    print(f'Pump was running for {round(running_mins)} minutes,\
 producing {round(gallons)} gallons')
    print('(That\'s {0} gallons per day)'.format(gallons_per_day))
    print(f'Pump required a total of {watts} watt minutes of power')
    print('(That\'s {0} kwhs)'.format(kwhs))
    print(f'It took {reach1} minutes of data to reach 5 gallons.')
    print(f'It took {reach2} minutes of data to reach 100 gallons.')

    # Print information on water softener recharges
    print()
    print('Information on water softener recharges:')
    for (x, y) in zip(long_run_mins, long_run_start):
        print(f'{x} minute run started at {y}')


main()
