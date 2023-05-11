import re


class TextCleaner:
    def __init__(self, file_string):
        self.file = file_string
        self.sentences = []
        self.cleaned_sentences = []

    def clean_text(self):

        # read file and strip the space in head and end
        text = self.file.strip().rstrip('.')

        # remove periods at the end of abbreviations
        text = re.sub(r"(Mr|Ms|Mrs|Dr|Prof|Rev|Hon|Sr|Jr)\.", r"\1", text)

        # convert all alphabetical characters to lowercase
        text = text.lower()

        # replace all commas with the token COMMA
        text = re.sub(r",", " COMMA ", text)

        # remove all other punctuation
        text = re.sub(r"[^.\w\s\']", "", text)

        # split text into sentences using regex pattern
        self.sentences = re.split(r'[.!?\n]+', text)
        self.cleaned_sentences = [i.strip() for i in self.sentences]
