import random


def password():
    """
    Producer: Jian Han
    Example:
    Welcome to the username and password generator!
    Please enter your first name: Ron
    Please enter your last name: Thomas
    Please enter your favorite word: Literature

    Thanks Ron, your user name is rthomas*81

    Here are three suggested passwords for you to consider:

    Password 1: r0n53th0m@$
    Password 2: rNtSlE
    Password 3: ThomaLitRo
    """
    #  Prompt the user for three pieces of information
    first_name = input('Please enter your first name:')
    last_name = input('Please enter your last name:')
    favorite_word = input('Please enter your favorite word:')

    # Produce a username for the user
    # Create a list for the seven letters of the last name,
    # then use the first seven letters from their last name
    # to replace the first seven element of the  list.
    seven_letters = ['*']*7
    for i in range(len(last_name)):
        seven_letters[i] = last_name[i]

    username = (first_name[0] + ''.join(seven_letters)
                + str(random.randrange(0, 100))).lower()
    print('Thanks Ron, your user name is ' + username)

    # Produce Password 1
    # a random integer in the range 0 – 99 between
    # # the first and last names, in lower case
    # 'a' should be replaced by @, o by 0, l by 1, and s by $.
    password_1 = []
    password_1[:] = (first_name + str(random.randrange(0, 100)) +
                     last_name).lower()
    for i in range(len(password_1)):
        if password_1[i] == 'a':
            password_1[i] = '@'
        elif password_1[i] == 'o':
            password_1[i] = '0'
        elif password_1[i] == 'l':
            password_1[i] = '1'
        elif password_1[i] == 's':
            password_1[i] = '$'
    print('Password 1: ' + ''.join(password_1))

    # Produce Password 2
    password_2 = first_name[0].lower() + \
        first_name[len(first_name) - 1].upper() + \
        last_name[0].lower() + \
        last_name[len(last_name) - 1].upper() + \
        favorite_word[0].lower() + \
        favorite_word[len(favorite_word) - 1].upper()
    print('Password 2: ' + password_2)

    # Produce Password 3
    password_3 = [first_name[0:random.randrange(1, len(first_name) + 1)],
                  last_name[0:random.randrange(1, len(first_name) + 1)],
                  favorite_word[0:random.randrange(1, len(first_name) + 1)],]
    random.shuffle(password_3)
    print('Password 3: ' + ''.join(password_3))


def main():
    password()


main()
