def fever_diagnosis():
    """An expert system to diagnose the cause of a fever."""
    # Get start the system
    print('Welcome to this expert system to diagnose the cause of a fever!')
    print('Please answer the questions below.')
    print('Please enter "Yes" or "No"')
    # Ask the inquirer some questions to diagnose the
    # possibilities of the cause of a fever
    if 'No' == input('Are you coughing? (Yes/No):'):
        if 'No' == input('Do you have a headche? (Yes/No):'):
            return aching()
        elif 'No' == input('Are you experiencing any of the following:'
                           ' pain when bending your head forward,'
                           ' nausea or vomiting, bright light hurting your'
                           ' eyes, drowsiness or confusion? (Yes/No):'):
            if 'No' == input('Are you vomiting or had diarrhea? (Yes/No):'):
                # Call the aching() function to continue the inquiry
                return aching()
            else:
                print('Possibilities include digestive tract infaction.')
        else:
            print('Possibilities include menigitis.')
    elif 'Yes' == input('Are you short of breath or wheezing '
                        'or coughing up phlegm? (Yes/No):'):
        print('Possibilities include pneumonia or infection of airways.')
    elif 'Yes' == input('Do you have a headache? (Yes/No):'):
        print('Possibilities include viral infection.')
    else:
        # Call the aching() function to continue the inquiry
        return aching()


def aching():
    """The step of the question about aching feeling
    of bones or joints to diagnose"""
    if 'Yes' == input('Do you have aching bones or aching joints? (Yes/No):'):
        print('Possibilities include viral infection.')
    elif 'Yes' == input('Do you have a rash? (Yes/No):'):
        print('Insufficient information to list possibilities.')
    elif 'Yes' == input('Do you have a sore throat? (Yes/No):'):
        print('Possibilities include a throat infection.')
    elif 'Yes' == input('Do you have back pain just above the waist '
                        'with chills and fever? (Yes/No):'):
        print('Possibilities include a kidney infection.')
    elif 'Yes' == input('Do you have pain urinating or are urinating more '
                        'often? (Yes/No):'):
        print('Possibilities include a urinary infection.')
    elif 'Yes' == input('Have you spent the day in the sun or in hot '
                        'conditions? (Yes/No):'):
        print('Possibilities sunstroke or heat exhaustion.')
    else:
        print('Insufficient information to list possibilities.')


def main():
    fever_diagnosis()


main()
