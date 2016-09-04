from antlr4 import FileStream, CommonTokenStream, InputStream
from generated.VhdlLexer import VhdlLexer
from generated.VhdlParser import VhdlParser
from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor
import nose


def setup_visitor(input_stream, start_rule):
    lexer = VhdlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    visitor = ConcreteVhdlVisitor()
    start_func = getattr(parser, start_rule)
    tree = start_func()
    visitor.visit(tree)
    return visitor


def parse_file(file_path, start_rule):
    input_stream = FileStream(file_path)
    return setup_visitor(input_stream, start_rule)


def parse_string(input_string, start_rule):
    input_stream = InputStream(input_string)
    return setup_visitor(input_stream, start_rule)


def test_sanity():
    parse_file('./assets/empty.vhd', 'design_file')
    parse_string('', 'design_file')
    nose.tools.ok_(True)


def test_name1():
    name = 'Adder'
    visitor = parse_string(name, 'name')
    nose.tools.eq_(visitor.name, 'Adder')


def test_name2():
    name = 'Adder.adder'
    visitor = parse_string(name, 'name')
    nose.tools.eq_(visitor.name, 'Adder.adder')
