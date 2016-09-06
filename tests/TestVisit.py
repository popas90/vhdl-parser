from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
import nose
from mockito import mock, when


class TestVisit:

    def test_identifier(self):
        visitor = ConcreteVhdlVisitor()
        identifier_node = mock()
        basic_identifier = mock()
        extended_identifier = mock()
        when(basic_identifier).getText().thenReturn('basic')
        when(extended_identifier).getText().thenReturn('extended')
        when(identifier_node).BASIC_IDENTIFIER().thenReturn(basic_identifier)
        nose.tools.eq_(visitor.visitIdentifier(identifier_node), 'basic')
        when(identifier_node).BASIC_IDENTIFIER().thenReturn(False)
        when(identifier_node).EXTENDED_IDENTIFIER().thenReturn(extended_identifier)
        nose.tools.eq_(visitor.visitIdentifier(identifier_node), 'extended')
