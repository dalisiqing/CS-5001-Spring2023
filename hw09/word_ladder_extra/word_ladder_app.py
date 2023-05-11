from word_ladder import WordLadder
import time


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    all_english_words = load_words()

    while True:
        w1, w2 = input("> ").split()
        # Create a WordLadder object
        wl = WordLadder(w1, w2, all_english_words)

        start_time = time.time()  # Record start time

        # Generate the word ladder
        word_ladder = wl.make_ladder()

        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time

        print("Ladder: ", word_ladder)
        print("Elapsed time: ", elapsed_time, " seconds")


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = set()
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            # Add to an existing set
            valid_words.add(w)

    return valid_words


main()
