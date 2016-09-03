from generated.VhdlListener import VhdlListener
from collections import deque


class ConcreteVhdlListener(VhdlListener):

    def __init__(self):
        self.name = ''
        self._parsing_stack = deque()

    def pop(self):
        return self._parsing_stack.pop()

    def peek(self):
        return self._parsing_stack[-1]

    def push(self, new_elem):
        self._parsing_stack.appendleft(new_elem)

    # name
    def enterName(self, ctx):
        self.push([])

    def exitName(self, ctx):
        self.name = ''.join(self.pop())

    # selected_name
    def enterSelected_name(self, ctx):
        pass

    def exitSelected_name(self, ctx):
        pass

    # identifier
    def enterIdentifier(self, ctx):
        self.peek().append(str(ctx.BASIC_IDENTIFIER()))

    def exitIdentifier(self, ctx):
        pass
