from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
from nose.tools import eq_
from mockito import mock, when
from src.Generic import Generic
from src.Operand import Operand
from src.Expression import Expression


class TestVisitor:

    # Helpers
    def setUp(self):
        self._visitor = ConcreteVhdlVisitor()
        self._ctx = mock()

    def _mock_for_visit(self, visit_result):
        mock_obj = mock()
        when(mock_obj).accept(self._visitor).thenReturn(visit_result)
        return mock_obj

    def _mock_list_for_visit(self, *visit_result):
        mock_list = []
        for result in visit_result:
            mock_list.append(self._mock_for_visit(result))
        return mock_list

    # This is unused, I was getting ready to refactor into it,
    # but couldn't find a good solution for calling methods
    # by name when mocking
    def set_mock_list(self, method, *visit_result):
        when(self._ctx).method() \
            .thenReturn(self._mock_list_for_visit(visit_result))

    # Tests
    def test_identifier(self):
        basic_identifier = mock()
        extended_identifier = mock()
        when(basic_identifier).getText().thenReturn('basic')
        when(extended_identifier).getText().thenReturn('extended')
        when(self._ctx).BASIC_IDENTIFIER().thenReturn(basic_identifier)
        when(self._ctx).EXTENDED_IDENTIFIER().thenReturn(extended_identifier)
        eq_('basic', self._visitor.visitIdentifier(self._ctx))
        when(self._ctx).BASIC_IDENTIFIER().thenReturn(False)
        eq_('extended', self._visitor.visitIdentifier(self._ctx))

    def test_identifier_list(self):
        when(self._ctx).identifier() \
            .thenReturn(self._mock_list_for_visit('id1', 'id2'))
        eq_(['id1', 'id2'], self._visitor.visitIdentifier_list(self._ctx))
        when(self._ctx).identifier() \
            .thenReturn(self._mock_list_for_visit('id1', 'id2', 'id3'))
        eq_(['id1', 'id2', 'id3'],
            self._visitor.visitIdentifier_list(self._ctx))

    def test_interface_constant_declaration(self):
        when(self._ctx).identifier_list() \
            .thenReturn(self._mock_for_visit(['gen1', 'gen2']))
        when(self._ctx).subtype_indication() \
            .thenReturn(self._mock_for_visit('type1'))
        eq_([Generic('gen1', 'type1'), Generic('gen2', 'type1')],
            self._visitor.visitInterface_constant_declaration(self._ctx))

    def test_name__name_part(self):
        when(self._ctx).name_part() \
            .thenReturn(self._mock_list_for_visit('part1'))
        eq_('part1', self._visitor.visitName__name_part(self._ctx))
        when(self._ctx).name_part() \
            .thenReturn(self._mock_list_for_visit('part1', 'part2', 'part3'))
        eq_('part1.part2.part3', self._visitor.visitName__name_part(self._ctx))

    def test_name__selected_name(self):
        when(self._ctx).selected_name() \
            .thenReturn(self._mock_for_visit('sel_name'))
        eq_('sel_name', self._visitor.visitName__selected_name(self._ctx))

    def test_selected_name(self):
        when(self._ctx).identifier().thenReturn(self._mock_for_visit('ident'))
        eq_('ident', self._visitor.visitSelected_name(self._ctx))
        when(self._ctx).suffix() \
            .thenReturn(self._mock_list_for_visit('suf'))
        eq_('ident.suf', self._visitor.visitSelected_name(self._ctx))
        when(self._ctx).suffix() \
            .thenReturn(self._mock_list_for_visit('suf', 'suf2'))
        eq_('ident.suf.suf2', self._visitor.visitSelected_name(self._ctx))

    def test_subtype_indication(self):
        when(self._ctx).selected_name() \
            .thenReturn(self._mock_list_for_visit('na', 'la', 'sa'))
        eq_(['na', 'la', 'sa'],
            self._visitor.visitSubtype_indication(self._ctx))
        when(self._ctx).constraint() \
            .thenReturn(self._mock_for_visit('constr'))
        eq_(['na', 'la', 'sa', 'constr'],
            self._visitor.visitSubtype_indication(self._ctx))

    def test_suffix__All(self):
        all_lit = mock()
        when(all_lit).getText().thenReturn('all')
        when(self._ctx).ALL().thenReturn(all_lit)
        eq_('all', self._visitor.visitSuffix__All(self._ctx))

    def test_suffix__Character_Literal(self):
        char_lit = mock()
        when(char_lit).getText().thenReturn("'lit'")
        when(self._ctx).CHARACTER_LITERAL().thenReturn(char_lit)
        eq_("'lit'", self._visitor.visitSuffix__Character_Literal(self._ctx))

    def test_suffix__identifier(self):
        when(self._ctx).identifier().thenReturn(self._mock_for_visit('ident'))
        eq_('ident', self._visitor.visitSuffix__identifier(self._ctx))

    def test_suffix__String_Literal(self):
        str_lit = mock()
        when(str_lit).getText().thenReturn('"str"')
        when(self._ctx).STRING_LITERAL().thenReturn(str_lit)
        eq_('"str"', self._visitor.visitSuffix__String_Literal(self._ctx))

    def test_simple_expression(self):
        plus = mock()
        minus = mock()
        when(plus).getText().thenReturn('+')
        when(minus).gettermText().thenReturn('-')
        when(self._ctx).PLUS().thenReturn(plus)
        when(self._ctx).MINUS().thenReturn(minus)
        when(self._ctx).term(0).thenReturn(self._mock_for_visit('3'))
        when(self._ctx).term().thenReturn(self._mock_list_for_visit('3'))
        eq_(Operand('+3'), self._visitor.visitSimple_expression(self._ctx))
        when(self._ctx).PLUS().thenReturn(None)
        eq_(Operand('-3'), self._visitor.visitSimple_expression(self._ctx))
        when(self._ctx).term().thenReturn(self._mock_list_for_visit('3', '2'))
        when(self._ctx).adding_operator() \
            .thenReturn(self._mock_list_for_visit('-'))
        eq_(-5, self._visitor.visitSimple_expression(self._ctx).evaluate())
        when(self._ctx).term() \
            .thenReturn(self._mock_list_for_visit('3', '2', '3'))
        when(self._ctx).adding_operator() \
            .thenReturn(self._mock_list_for_visit('-', '+'))
        eq_(-2, self._visitor.visitSimple_expression(self._ctx).evaluate())

    def test_term(self):
        when(self._ctx).factor(0).thenReturn(self._mock_for_visit('3'))
        when(self._ctx).factor().thenReturn(self._mock_list_for_visit('3'))
        eq_(Operand('+3'), self._visitor.visitTerm(self._ctx))
        when(self._ctx).factor() \
            .thenReturn(self._mock_list_for_visit('3', '2'))
        when(self._ctx).multiplying_operator() \
            .thenReturn(self._mock_list_for_visit('*'))
        eq_(6, self._visitor.visitTerm(self._ctx).evaluate())

    def test_factor(self):
        when(self._ctx).primary(0).thenReturn(self._mock_for_visit('2'))
        eq_('2', self._visitor.visitFactor(self._ctx))
        when(self._ctx).primary(0).thenReturn(self._mock_for_visit('3'))
        eq_('3', self._visitor.visitFactor(self._ctx))
        when(self._ctx).primary(1).thenReturn(self._mock_for_visit('3'))
        eq_('3**3', self._visitor.visitFactor(self._ctx))
        when(self._ctx).primary(1).thenReturn(None)
        not_ = mock()
        abs_ = mock()
        when(not_).getText().thenReturn('not')
        when(abs_).getText().thenReturn('abs')
        when(self._ctx).NOT().thenReturn(not_)
        eq_('not 3', self._visitor.visitFactor(self._ctx))
        when(self._ctx).NOT().thenReturn(None)
        when(self._ctx).ABS().thenReturn(abs_)
        eq_('abs 3', self._visitor.visitFactor(self._ctx))

    def test_primary(self):
        when(self._ctx).expression().thenReturn(self._mock_for_visit('expr'))
        eq_('(expr)', self._visitor.visitPrimary(self._ctx))

    def test_shift_expression(self):
        when(self._ctx).simple_expression(0) \
            .thenReturn(self._mock_for_visit('2'))
        when(self._ctx).simple_expression() \
            .thenReturn(self._mock_list_for_visit('2'))
        eq_(Operand('2'), self._visitor.visitShift_expression(self._ctx))
        when(self._ctx).simple_expression() \
            .thenReturn(self._mock_list_for_visit('2', '4'))
        when(self._ctx).shift_operator() \
            .thenReturn(self._mock_list_for_visit('sll'))
        eq_(Expression('2', '4', 'sll'),
            self._visitor.visitShift_expression(self._ctx))

    def test_relation(self):
        when(self._ctx).shift_expression(0) \
            .thenReturn(self._mock_for_visit('2'))
        when(self._ctx).shift_expression() \
            .thenReturn(self._mock_list_for_visit('2'))
        eq_(Operand('2'), self._visitor.visitRelation(self._ctx))
        when(self._ctx).shift_expression() \
            .thenReturn(self._mock_list_for_visit('2', '4'))
        when(self._ctx).relational_operator() \
            .thenReturn(self._mock_list_for_visit('>'))
        eq_(Expression('2', '4', '>'),
            self._visitor.visitRelation(self._ctx))

    def test_expression(self):
        when(self._ctx).relation(0) \
            .thenReturn(self._mock_for_visit('2'))
        when(self._ctx).relation() \
            .thenReturn(self._mock_list_for_visit('2'))
        eq_(Operand('2'), self._visitor.visitExpression(self._ctx))
        when(self._ctx).relation() \
            .thenReturn(self._mock_list_for_visit('2', '4'))
        when(self._ctx).logical_operator() \
            .thenReturn(self._mock_list_for_visit('and'))
        eq_(Expression('2', '4', 'and'),
            self._visitor.visitExpression(self._ctx))
