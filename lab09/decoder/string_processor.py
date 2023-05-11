from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self, str):
        self.stack = Stack()
        self.string_to_process = str
        self.solution = ''

    def process_string(self):
        for i in self.string_to_process:
            if i == '*' and self.stack.peek():
                self.solution += self.stack.pop()
            elif i == '^' and self.stack.peek():
                self.solution += self.stack.pop()
                if self.stack.peek():
                    self.solution += self.stack.pop()
                else:
                    self.solution = self.solution[:-1]
            elif i != '*' and i != '^':
                self.stack.push(i)
            else:
                continue
        return self.solution
