import random


def main():
    print('Welcome to the DMV (estimated wait time is 3 hours)')
    name = input('Please enter your first, middle, and last name:\n').split(' ', 2)
    LN = name[2]
    FN = name[0] + ' ' + name[1]

    DOB = input('Enter date of birth (MM/DD/YY):\n')
    birthday = DOB.split('/', 2)
    EXP_year = '21'
    EXP = birthday[0] + '/' + birthday[1] + '/' + EXP_year

    DL = ''
    for i in range(0, 7):
        DL += str(random.randint(0, 9))
    print('-------------------------------------\nWashington Driver License')
    print(f'DL {DL}')
    print(f'LN {LN}')
    print(f'FN {FN}')
    print(f'DOB {DOB}')
    print(f'EXP {EXP}')
    print('-------------------------------------')


main()
