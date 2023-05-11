import sys
from ngram_frequencies import NgramFrequencies
from text_cleaner import TextCleaner


def main(file):
    with open(file, 'r') as t:
        cleaned_t = TextCleaner(t.read())
        cleaned_t.clean_text()
        unigrams = NgramFrequencies(1, cleaned_t.cleaned_sentences)
        bigrams = NgramFrequencies(2, cleaned_t.cleaned_sentences)
        trigrams = NgramFrequencies(3, cleaned_t.cleaned_sentences)
        print("Top 10 unigrams:")
        print_output(unigrams.top_n_freqs(10))
        print("Top 10 bigrams:")
        print_output(bigrams.top_n_freqs(10))
        print("Top 10 trigrams:")
        print_output(trigrams.top_n_freqs(10))


def print_output(collection):
    for item in collection:
        print(f"\t{item}")


main(sys.argv[1])
