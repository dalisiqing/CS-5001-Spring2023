import random
import math


def main():
    random_number = random.randint(0, 50)
    print(f'secret number is {random_number}')
    print('Welcome to the Guessing Game!')
    user_guess = int(input('I picked a number between and 50. Try and guess!\n'))
    print(f'You guessed {user_guess}')
    tries = 0
    while (random_number != user_guess):
        far_off = math.fabs(random_number - user_guess)
        if far_off <=1:
            print('Your guess is scalding hot')
        elif 1 < far_off <= 2:
            print('Your guess is extremely warm')
        elif 2 < far_off <= 3:
            print('Your guess is very warm')
        elif 3 < far_off <= 5:
            print('Your guess is warm')
        elif 5 < far_off <= 8:
            print('Your guess is cold')
        elif 8 < far_off <= 13:
            print('Your guess is very cold')
        elif 13 < far_off <= 20:
            print('Your guess is extremely cold')
        else:
            print('Your guess is icy freezing miserably cold')
        user_guess = int(input())
        tries += 1
    print(f'Congratulations. You figured it out in {tries} tries.')
    if tries == 1:
        print("That was lucky!")
    elif 2 <= tries <= 4:
        print("That was amazing!")
    elif 5 <= tries <= 6:
        print("That was okay.")
    elif tries == 7:
        print("Meh.")
    elif 8 <= tries <= 9:
        print("This is not your game.")
    elif 10 <= tries:
        print("You are the worst guesser I've ever seen.")


main()
