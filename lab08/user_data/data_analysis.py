import re


class DataAnalysis:

    def __init__(self, file):
        # TODO: set up the necessary instance variables
        self.lang_counts = {}
        self.line_total = -1
        self.cnt_counts = {}
        self.read_data(file)

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        # read the data of file
        try:
            f = open(file_name)
        except FileNotFoundError:
            print("Can't find", file_name)
            return
        # Process each line of text and
        # add matched language and country
        # to the corresponding dictionaries to get the counts
        for line in f:
            self.line_total += 1
            p = re.compile(r'[A-Z]{1}[a-z íā]+$', re.M)
            for lang in p.findall(line):
                self.add_lang(lang)

            q = re.compile(r'\.([a-z]{2}),', re.M)
            for cnt in q.findall(line):
                self.add_cnt(cnt)

    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, N):
        return self.sorted_freqs(self.lang_counts, self.line_total)[:N]

    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered 
    # from highest frequency to lowest.

    def top_n_country_tlds_freqs(self, N):
        return self.sorted_freqs(self.cnt_counts, self.line_total)[:N]

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.
    def add_lang(self, lang):
        """Add a language to the lang_counts dictionary"""
        if lang in self.lang_counts.keys():
            self.lang_counts[lang] += 1
        else:
            self.lang_counts[lang] = 1

    def add_cnt(self, cnt):
        """Add a country to the cnt_counts dictionary"""
        if cnt in self.cnt_counts.keys():
            self.cnt_counts[cnt] += 1
        else:
            self.cnt_counts[cnt] = 1

    def freqs(self, x_counts, x_total):
        """Return a dictionary of frequencies"""
        return {k: x_counts[k]/x_total for k in x_counts.keys()}

    def sorted_freqs(self, x_counts, x_total):
        """Return a list of sorted freqs"""
        return sorted(
            self.freqs(x_counts, x_total).items(),
            key=lambda x: x[1],
            reverse=True
        )
