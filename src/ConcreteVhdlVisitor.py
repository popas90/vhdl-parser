from generated.VhdlVisitor import VhdlVisitor
from .Entity import Entity
from .Generic import Generic
from .Operand import Operand
from .Expression import Expression


class ConcreteVhdlVisitor(VhdlVisitor):

    def __init__(self):
        self.entities = []

    def visitAbstract_literal__Integer(self, ctx):
        return ctx.INTEGER().getText()

    def visitAbstract_literal__Real_Literal(self, ctx):
        return ctx.REAL_LITERAL().getText()

    def visitAdding_operator(self, ctx):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        if ctx.MINUS():
            return ctx.MINUS().getText()
        return ctx.AMPERSAND().getText()

    def visitDirection(self, ctx):
        if ctx.TO():
            return ctx.TO().getText().lower()
        return ctx.DOWNTO().getText().lower()

    def visitEnumeration_literal__Character_Literal(self, ctx):
        return ctx.CHARACTER_LITERAL().getText().lower()

    def visitEntity_declaration(self, ctx):
        self.entities.append(Entity(self.visit(ctx.identifier()[0])))

    def visitIdentifier(self, ctx):
        if ctx.BASIC_IDENTIFIER():
            return ctx.BASIC_IDENTIFIER().getText()
        return ctx.EXTENDED_IDENTIFIER().getText()

    def visitIdentifier_list(self, ctx):
        return [self.visit(ident) for ident in ctx.identifier()]

    def visitInterface_constant_declaration(self, ctx):
        identifiers = self.visit(ctx.identifier_list())
        type_ind = ''.join(self.visit(ctx.subtype_indication()))
        generics = [Generic(ident, type_ind) for ident in identifiers]
        return generics

    def visitLiteral__Bit_String_Literal(self, ctx):
        return ctx.BIT_STRING_LITERAL().getText().lower()

    def visitLiteral__Null(self, ctx):
        return ctx.NULL().getText().lower()

    def visitLiteral__enumeration_literal(self, ctx):
        return self.visit(ctx.enumeration_literal()).lower()

    def visitLogical_operator(self, ctx):
        if ctx.AND():
            return ctx.AND().getText().lower()
        if ctx.OR():
            return ctx.OR().getText().lower()
        if ctx.NAND():
            return ctx.NAND().getText().lower()
        if ctx.NOR():
            return ctx.NOR().getText().lower()
        if ctx.XOR():
            return ctx.XOR().getText().lower()
        return ctx.XNOR().getText().lower()

    def visitMultiplying_operator(self, ctx):
        if ctx.MUL():
            return ctx.MUL().getText()
        if ctx.DIV():
            return ctx.DIV().getText()
        if ctx.MOD():
            return ctx.MOD().getText().lower()
        return ctx.REM().getText().lower()

    def visitName__name_part(self, ctx):
        parts = ''
        for part in ctx.name_part():
            parts += self.visit(part) + '.'
        # remove trailing '.'
        return parts[:-1]

    def visitName__selected_name(self, ctx):
        return self.visit(ctx.selected_name())

    def visitRelational_operator(self, ctx):
        if ctx.EQ():
            return ctx.EQ().getText().lower()
        if ctx.NEQ():
            return ctx.NEQ().getText().lower()
        if ctx.LOWERTHAN():
            return ctx.LOWERTHAN().getText().lower()
        if ctx.LE():
            return ctx.LE().getText().lower()
        if ctx.GREATERTHAN():
            return ctx.GREATERTHAN().getText().lower()
        return ctx.GE().getText().lower()

    def visitSelected_name(self, ctx):
        string = self.visit(ctx.identifier())
        if ctx.suffix():
            for suf in ctx.suffix():
                string += '.' + self.visit(suf)
        return string

    def visitShift_operator(self, ctx):
        if ctx.SLL():
            return ctx.SLL().getText().lower()
        if ctx.SRL():
            return ctx.SRL().getText().lower()
        if ctx.SLA():
            return ctx.SLA().getText().lower()
        if ctx.SRA():
            return ctx.SRA().getText().lower()
        if ctx.ROR():
            return ctx.ROR().getText().lower()
        return ctx.ROL().getText().lower()

    def visitSimple_expression(self, ctx):
        sign = '+' if ctx.PLUS() else '-' if ctx.MINUS() else ''
        first_term = ctx.term(0)
        # terms = [self.visit(term) for term in ctx.term()]
        prev_expr = Operand(sign + self.visit(first_term))
        if len(ctx.term()) == 1:
            return prev_expr
        other_terms = ctx.term()[1:]
        for (op, term) in zip(ctx.adding_operator(), other_terms):
            current_op = Operand(self.visit(term))
            prev_expr = Expression(prev_expr, current_op, self.visit(op))
        return prev_expr

    def visitSubtype_indication(self, ctx):
        subtype = [self.visit(sel_name) for sel_name in ctx.selected_name()]
        if (ctx.constraint()):
            subtype.append(self.visit(ctx.constraint()))
        return subtype

    def visitSuffix__All(self, ctx):
        return ctx.ALL().getText()

    def visitSuffix__Character_Literal(self, ctx):
        return ctx.CHARACTER_LITERAL().getText()

    def visitSuffix__identifier(self, ctx):
        return self.visit(ctx.identifier())

    def visitSuffix__String_Literal(self, ctx):
        return ctx.STRING_LITERAL().getText()

    def visitTerm(self, ctx):
        first_factor = self.visit(ctx.factor(0))
        prev_expr = Operand(first_factor)
        if len(ctx.factor()) == 1:
            return prev_expr
        other_factors = ctx.factor()[1:]
        for (op, factor) in zip(ctx.multiplying_operator(), other_factors):
            current_op = Operand(self.visit(factor))
            prev_expr = Expression(prev_expr, current_op, self.visit(op))
        return prev_expr
