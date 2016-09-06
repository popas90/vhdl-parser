from antlr4 import FileStream, CommonTokenStream, InputStream
from generated.VhdlLexer import VhdlLexer
from generated.VhdlParser import VhdlParser
from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
import nose
from mockito import mock, when


def setup_visitor(input_stream, start_rule):
    lexer = VhdlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    visitor = ConcreteVhdlVisitor()
    start_func = getattr(parser, start_rule)
    tree = start_func()
    visitor.visit(tree)
    return visitor


def parse_file(file_path, start_rule='design_file'):
    input_stream = FileStream(file_path)
    return setup_visitor(input_stream, start_rule)


def parse_string(input_string, start_rule='design_file'):
    input_stream = InputStream(input_string)
    return setup_visitor(input_stream, start_rule)


def test_sanity():
    parse_file('./assets/empty.vhd', 'design_file')
    parse_string('', 'design_file')
    nose.tools.ok_(True)


def test_name_1():
    name = 'Adder'
    visitor = parse_string(name, 'name')
    nose.tools.eq_(visitor.name, 'Adder')


def test_name_2():
    name = 'Adder.adder.add'
    visitor = parse_string(name, 'name')
    nose.tools.eq_(visitor.name, 'Adder.adder.add')


def test_entity_declaration_empty():
    entity = """entity Adder is
             end entity Adder;"""
    visitor = parse_string(entity)
    nose.tools.eq_(visitor.entities[0].name, 'Adder')

# TODO keep this out until mocking is in place
"""
def test_port_declaration():
    entity = ""entity Adder is
             port(rst : in std_logic)
             end entity Adder;""
    visitor = parse_string(entity)
    nose.tools.eq_(visitor.entities[0].ports[0].name, 'rst')
    nose.tools.eq_(visitor.entities[0].ports[0].direction, 'in')
    nose.tools.eq_(visitor.entities[0].ports[0].type, 'std_logic')
"""


def test_identifier():
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
