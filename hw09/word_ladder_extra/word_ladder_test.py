from word_ladder import WordLadder


# TODO: Write appropriate unit tests
def test_make_ladder():
    valid_words = set()
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            # Add to an existing set
            valid_words.add(w)
    t1 = WordLadder('normal', 'special', valid_words)
    assert t1.make_ladder().items == ['normal', 'norma', 'noma', 'soma',
                                      'some', 'same', 'sate', 'spate',
                                      'spathe', 'spathae', 'spathal',
                                      'spatial', 'spacial', 'special']

    t2 = WordLadder('long', 'short', valid_words)
    assert t2.make_ladder().items == ['long', 'hong', 'hont', 'hort', 'short']

    t3 = WordLadder('cat', 'haa', valid_words)
    assert t3.make_ladder() is None
