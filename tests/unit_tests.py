from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream
from generated.VhdlLexer import VhdlLexer
from generated.VhdlParser import VhdlParser
from src.ConcreteVhdlListener import ConcreteVhdlListener
import nose


def setup_listener(input_stream, start_rule):
    lexer = VhdlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = ConcreteVhdlListener()
    start_func = getattr(parser, start_rule)
    tree = start_func()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def setup_file_parse(file_path, start_rule):
    input_stream = FileStream(file_path)
    return setup_listener(input_stream, start_rule)


def setup_string_parse(input_string, start_rule):
    input_stream = InputStream(input_string)
    return setup_listener(input_stream, start_rule)


def test_empty():
    setup_file_parse('./assets/empty.vhd', 'design_file')
    nose.tools.ok_(True)


def test_name1():
    name = 'Adder'
    listener = setup_string_parse(name, 'name')
    nose.tools.eq_(listener.name, 'Adder')


def test_name2():
    name = 'Adder.adder'
    listener = setup_string_parse(name, 'name')
    nose.tools.eq_(listener.name, 'Adder.adder')
