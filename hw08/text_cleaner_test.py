from text_cleaner import TextCleaner


def test_constructor():
    """Test the constructor"""
    test_text = "abc"
    t = TextCleaner(test_text)
    t.file == test_text
    t.sentences == []
    t.cleaned_sentences == []


def test_clean_text():
    test_text = """ Directed by Mr. Burton and Mike Johnson, and written by John August, Caroline Thompson and Pamela Pettler, the story hangs on a timid bachelor with matchstick legs and a pallid complexion, Victor (voiced by Johnny Depp), whose upwardly mobile parents arrange his marriage to Victoria (Emily Watson), the retiring daughter of impoverished gentry. When the wedding rehearsal goes kablooey, Victor retreats into the woods, whereupon he becomes the reluctant object of desire of the Corpse Bride, a blue-tinted beauty with gnawed-through limbs and a miraculously preserved bosom (Helena Bonham Carter, the director's very alive partner). """
    t = TextCleaner(test_text)
    t.clean_text()
    test_cleaned_sentences = ['directed by mr burton and mike johnson COMMA  and written by john august COMMA  caroline thompson and pamela pettler COMMA  the story hangs on a timid bachelor with matchstick legs and a pallid complexion COMMA  victor voiced by johnny depp COMMA  whose upwardly mobile parents arrange his marriage to victoria emily watson COMMA  the retiring daughter of impoverished gentry', "when the wedding rehearsal goes kablooey COMMA  victor retreats into the woods COMMA  whereupon he becomes the reluctant object of desire of the corpse bride COMMA  a bluetinted beauty with gnawedthrough limbs and a miraculously preserved bosom helena bonham carter COMMA  the director's very alive partner"]
    for i in range(len(t.cleaned_sentences)):
        assert t.cleaned_sentences[i] == test_cleaned_sentences[i]
