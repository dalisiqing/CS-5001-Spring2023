from queue import Queue
from stack import Stack
import string


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        self.queue = Queue()
        self.stack = Stack()
        self.usedwords = set()
        self.alpahbet = list(string.ascii_lowercase)
        # Initialize a queue containing a single
        # stack, which in turn contains the first word in the word ladder
        self.stack.push(w1)
        self.queue.enqueue(self.stack)
        self.last_word = w2
        self.wordlist = wordlist

    def make_ladder(self):
        # For each element in the queue
        while not self.queue.isEmpty():
            # Dequeue the element, which is a beginning stack to test
            stack_to_test = self.queue.dequeue()
            # print(f'this is a test: {stack_to_test}')
            # Peek at its top item (a word). For each character in the word
            word = list(stack_to_test.peek())
            self.usedwords.add(''.join(word))
            # print('this is a new word: ' + ''.join(word))
            for c in range(len(word)):
                # For each letter in the alpahbet
                for i in self.alpahbet:
                    # Replace the character with that letter to generate a
                    # candidate new word
                    new_word_list = word[:]
                    new_word_list[c] = i
                    new_word = ''.join(new_word_list)
                    # Check the candidate to see if it is an English word
                    # Check whether the candidate is in usedwords
                    if new_word in self.wordlist and new_word not in\
                            self.usedwords:
                        self.usedwords.add(new_word)
                        # Make a duplicate of the stack and
                        # push the new word onto the new stack
                        self.new_stack = stack_to_test.copy()
                        self.new_stack.push(new_word)
                        if new_word == self.last_word:
                            return self.new_stack
                        else:
                            self.queue.enqueue(self.new_stack)
                        # print(f'this is a new stack {self.new_stack}')
                # print(f'end of {c}')

        return None
