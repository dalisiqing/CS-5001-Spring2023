class NgramFrequencies:
    def __init__(self, n, sentences):
        self.total = 0
        self.num = n
        self.sentences = sentences
        self.counts = {}
        self.add_item(self.num, self.sentences)

    def add_item(self, num, sentences):
        """Add a gram to the counts dictionary"""
        for sentence in sentences:
            words = sentence.split()
            for i in range(len(words) - num + 1):
                self.total += 1
                gram = "_".join(words[i:i + num])
                if gram in self.counts.keys():
                    self.counts[gram] += 1
                else:
                    self.counts[gram] = 1

    def top_n_counts(self, n):
        """Return list of sorted n counts
        with the most frequent first"""
        return sorted(self.counts.items(), key=lambda x: self.frequency(x),
                      reverse=True)[:n]

    def top_n_freqs(self, n):
        return [(k[0], self.frequency(k)) for k in self.top_n_counts(n)]

    def frequency(self, item):
        """Return dictionary of frequencies as property"""
        ROUND_PLACES = 3
        return round(item[1]/self.total, ROUND_PLACES)
