from word_ladder import WordLadder


# TODO: Write appropriate unit tests
def test_make_ladder():
    wordlist1 = {'bat', 'dat', 'eat', 'fat', 'gat', 'hat'}
    t1 = WordLadder('cat', 'hat', wordlist1)
    assert t1.make_ladder().items == ['cat', 'hat']

    wordlist2 = {'love', 'hove', 'have', 'hate', 
                 'bove', 'boce', 'soce', 'cove', 
                 'cave', 'cace', 'gove', 'gave', 'gabe'}
    t2 = WordLadder('love', 'hate', wordlist2)
    assert t2.make_ladder().items == ['love', 'hove', 'have', 'hate']

    t3 = WordLadder('cat', 'haa', wordlist1)
    assert t3.make_ladder() is None

    t4 = WordLadder('cat', 'hatt', wordlist1)
    assert t4.make_ladder() is None
