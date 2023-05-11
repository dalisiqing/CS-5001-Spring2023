from ngram_frequencies import NgramFrequencies


def test_constructor():
    """Test the constructor"""

    text_test = ['this is a first test',
                 'this is not the first test', 'this is another test']

    bigrams = NgramFrequencies(2, text_test)

    num = 2
    total = 12
    this_is_count = 3
    first_text_count = 2
    a_first_count = 1

    assert bigrams.total == total
    assert bigrams.num == num
    assert bigrams.sentences == text_test
    assert bigrams.counts['this_is'] == this_is_count
    assert bigrams.counts['first_test'] == first_text_count
    assert bigrams.counts['a_first'] == a_first_count


def test_top_n_counts():
    text_test = ['this is a first test',
                 'this is not the first test', 'this is another test']
    bigrams = NgramFrequencies(2, text_test)
    num_3 = 3
    num_2 = 2
    bigrams.top_n_counts(3)[0][1] == num_3
    bigrams.top_n_counts(3)[1][1] == num_2


def test_top_n_freqs():
    text_test = ['this is a first test',
                 'this is not the first test', 'this is another test']
    bigrams = NgramFrequencies(2, text_test)
    item_0 = ('this_is', 0.25)
    item_1 = ('first_test', 0.167)
    bigrams.top_n_freqs(3)[0][0] == item_0[0]
    bigrams.top_n_freqs(3)[1][1] == item_1[1]


def test_frequency():
    text_test = ['this is a first test',
                 'this is not the first test', 'this is another test']
    bigrams = NgramFrequencies(2, text_test)
    t = [('this_is', 3), ('is_a', 1), ('a_first', 1), ('first_test', 2), ('is_not', 1),
         ('not_the', 1), ('the_first', 1), ('is_another', 1), ('another_test', 1)]
    item_0 = ('this_is', 0.25)
    item_1 = ('first_test', 0.167)
    bigrams.frequency(t[0]) == item_0[1]
    bigrams.frequency(t[3]) == item_1[1]
