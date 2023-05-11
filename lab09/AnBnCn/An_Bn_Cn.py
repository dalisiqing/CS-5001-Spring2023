from stack_python_list import Stack  # nopep8


class AnBnCn:
    """Class for evaluating strings of N a's followed by N b's followed by
      N c's"""

    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()
        self.stack_c = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        # TODO:
        # Return True if in_string matches a^nb^n pattern
        # False otherwise
        for char in in_string:
            if (char == 'a' and self.stack_b.is_empty()
                    and self.stack_c.is_empty()):
                self.stack_a.push(char)
            elif char == 'b':
                if self.stack_a.is_empty():
                    return False
                else:
                    self.stack_a.pop()
                    self.stack_b.push(char)
            elif char == 'c':
                if self.stack_b.is_empty() or not self.stack_a.is_empty():
                    return False
                else:
                    self.stack_b.pop()
                    self.stack_c.push(char)
            else:
                return False
        return self.stack_a.is_empty()

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack_a = Stack()
        self.stack_b = Stack()
        self.stack_c = Stack()
