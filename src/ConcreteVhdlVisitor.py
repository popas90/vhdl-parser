from generated.VhdlVisitor import VhdlVisitor
from .Entity import Entity


class ConcreteVhdlVisitor(VhdlVisitor):

    def __init__(self):
        self.name = ''
        self.entities = []

    def visitEntity_declaration(self, ctx):
        self.entities.append(Entity(self.visit(ctx.identifier()[0])))

    def visitIdentifier(self, ctx):
        if ctx.BASIC_IDENTIFIER():
            return ctx.BASIC_IDENTIFIER().getText()
        else:
            return ctx.EXTENDED_IDENTIFIER().getText()

    def visitName__name_part(self, ctx):
        parts = ''
        for part in ctx.name_part():
            parts += self.visit(part) + '.'
        # remove trailing '.'
        return parts[:-1]

    def visitName__selected_name(self, ctx):
        self.name = self.visit(ctx.selected_name())
        return self.name

    def visitSelected_name(self, ctx):
        string = self.visit(ctx.identifier())
        if ctx.suffix():
            for suf in ctx.suffix():
                string += '.' + self.visit(suf)
        return string

    def visitSuffix__All(self, ctx):
        return ctx.ALL().getText()

    def visitSuffix__Character_Literal(self, ctx):
        return ctx.CHARACTER_LITERAL().getText()

    def visitSuffix__identifier(self, ctx):
        return self.visit(ctx.identifier())

    def visitSuffix__String_Literal(self, ctx):
        return ctx.STRING_LITERAL().getText()
