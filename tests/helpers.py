import nose
from antlr4 import FileStream, CommonTokenStream, InputStream
from generated.VhdlLexer import VhdlLexer
from generated.VhdlParser import VhdlParser
from src.ConcreteVhdlVisitor import ConcreteVhdlVisitor


def _setup_parser_visitor(input_stream):
    """Given an input stream, returns parser and visitor objects."""
    lexer = VhdlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    visitor = ConcreteVhdlVisitor()
    return (parser, visitor)


def _run_rule(parser, visitor, start_rule, global_state):
    """Runs the visitor, starting from the given rule. If global_state is
    set to True, then it will return the Visitor object, in order to see
    its global state. Otherwise, the result of the rule being visited is
    returned.
    """
    start_func = getattr(parser, start_rule)
    tree = start_func()
    if global_state:
        visitor.visit(tree)
        return visitor
    else:
        return visitor.visit(tree)


def parse_file(file_path):
    """Parses and visits a VHDL file.Always starts from main rule."""
    input_stream = FileStream(file_path)
    parser, visitor = _setup_parser_visitor(input_stream)
    return _run_rule(parser, visitor, 'design_file', True)


def parse_string(input_string, start_rule='design_file', global_state=False):
    """Parses and visits a string. Start rule can be given as parameter.
    Can return actual Visitor object or the result returned by the visited
    rule (by setting global_state to False).
    """
    input_stream = InputStream(input_string)
    parser, visitor = _setup_parser_visitor(input_stream)
    return _run_rule(parser, visitor, start_rule, global_state)


def check_visitor_return(input_str, rule, expected):
    """Checks the result returned by running the visitor for the specified
    rule, with the given input. Compares the return value with expected.
    """
    visit_result = parse_string(input_str, rule)
    nose.tools.eq_(expected, visit_result)
