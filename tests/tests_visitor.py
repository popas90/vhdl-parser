from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
from nose.tools import eq_
from mockito import mock, when


class TestVisitor:

    def setUp(self):
        self._visitor = ConcreteVhdlVisitor()
        self._ctx = mock()

    def mock_for_visit(self, visit_result):
        mock_obj = mock()
        when(mock_obj).accept(self._visitor).thenReturn(visit_result)
        return mock_obj

    def test_identifier(self):
        basic_identifier = mock()
        extended_identifier = mock()
        when(basic_identifier).getText().thenReturn('basic')
        when(extended_identifier).getText().thenReturn('extended')
        when(self._ctx).BASIC_IDENTIFIER().thenReturn(basic_identifier)
        when(self._ctx).EXTENDED_IDENTIFIER().thenReturn(extended_identifier)
        eq_(self._visitor.visitIdentifier(self._ctx), 'basic')
        when(self._ctx).BASIC_IDENTIFIER().thenReturn(False)
        eq_(self._visitor.visitIdentifier(self._ctx), 'extended')

    def test_suffix__All(self):
        all_lit = mock()
        when(all_lit).getText().thenReturn('all')
        when(self._ctx).ALL().thenReturn(all_lit)
        eq_(self._visitor.visitSuffix__All(self._ctx), 'all')

    def test_suffix__Character_Literal(self):
        char_lit = mock()
        when(char_lit).getText().thenReturn("'lit'")
        when(self._ctx).CHARACTER_LITERAL().thenReturn(char_lit)
        eq_(self._visitor.visitSuffix__Character_Literal(self._ctx), "'lit'")

    def test_suffix__identifier(self):
        when(self._ctx).identifier().thenReturn(self.mock_for_visit('ident'))
        eq_(self._visitor.visitSuffix__identifier(self._ctx), 'ident')

    def test_suffix__String_Literal(self):
        str_lit = mock()
        when(str_lit).getText().thenReturn('"str"')
        when(self._ctx).STRING_LITERAL().thenReturn(str_lit)
        eq_(self._visitor.visitSuffix__String_Literal(self._ctx), '"str"')
