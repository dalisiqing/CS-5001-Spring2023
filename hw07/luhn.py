def validate(x):
    """
    Verify the user input account number
    """
    for i in range(len(x) - 2, -1, -2):
        x[i] *= 2
        if x[i] > 9:
            x[i] = x[i] % 10 + x[i] // 10
    if sum(x) % 10 == 0:
        print("Your account number is valid")
    else:
        print("Your account number is not valid")


def main():
    """
    Prompt the user to enter an account number and verify it
    """
    acc_number_list = [int(i) for i in
                       input('Please enter your account number:\n')]
    validate(acc_number_list)


main()
