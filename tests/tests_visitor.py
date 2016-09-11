from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
from nose.tools import eq_
from mockito import mock, when


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
