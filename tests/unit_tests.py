from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from generated.vhdlLexer import vhdlLexer
from generated.vhdlParser import vhdlParser
from generated.vhdlListener import vhdlListener
import nose


def parse_file_setup(file_path):
    inp = FileStream(file_path)
    lexer = vhdlLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = vhdlParser(stream)
    listener = vhdlListener()
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def test_empty():
    parse_file_setup('./assets/empty.vhd')
    nose.tools.ok_(True)
