from generated.VhdlVisitor import VhdlVisitor


class ConcreteVhdlVisitor(VhdlVisitor):

    def __init__(self):
        self.name = ''

    def visitName__selected_name(self, ctx):
        self.name = self.visit(ctx.selected_name())

    def visitSelected_name(self, ctx):
        string = self.visit(ctx.identifier())
        if ctx.suffix():
            for suf in ctx.suffix():
                string += '.' + self.visit(suf)
        return string

    def visitSuffix__identifier(self, ctx):
        return self.visit(ctx.identifier())

    def visitIdentifier(self, ctx):
        if ctx.BASIC_IDENTIFIER():
            return ctx.BASIC_IDENTIFIER().getText()
        else:
            return ctx.EXTENDED_IDENTIFIER().getText()
