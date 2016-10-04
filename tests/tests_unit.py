import nose
from helpers import parse_file, parse_string, check_visitor_return
from src.Generic import Generic


def test_sanity():
    parse_file('./assets/empty.vhd')
    parse_string('', 'design_file')
    nose.tools.ok_(True)


def test_entity_declaration_empty():
    entity = 'entity Adder is end entity Adder;'
    visitor = parse_string(entity, 'design_file', True)
    nose.tools.eq_(visitor.entities[0].name, 'Adder')


def test_generic_declaration():
    generic = 'kDepth : natural := 8'
    check_visitor_return(generic, 'interface_constant_declaration',
                         [Generic('kDepth', 'natural', '8')])


def test_abstract_literal():
    # ignoring BASE_LITERAL option for now
    check_visitor_return('22', 'abstract_literal', '22')
    check_visitor_return('22.33', 'abstract_literal', '22.33')


def test_numeric_literal():
    # ignoring PHYSICAL_LITERAL option for now
    check_visitor_return('52.3', 'numeric_literal', '52.3')


def test_literal():
    check_visitor_return('nULl', 'literal', 'null')
    check_visitor_return('b1010', 'literal', 'b1010')
    check_visitor_return('B"1010"', 'literal', 'b"1010"')
    check_visitor_return('1019', 'literal', '1019')
    check_visitor_return('hC1A1F', 'literal', 'hc1a1f')
    check_visitor_return('xAABB', 'literal', 'xaabb')


def test_enumeration_literal():
    check_visitor_return('this', 'enumeration_literal', 'this')
    check_visitor_return("'l'",  'enumeration_literal', "'l'")


def test_primary():
    check_visitor_return('b1011', 'primary', 'b1011')


def test_direction():
    check_visitor_return('to', 'direction', 'to')
    check_visitor_return('DOWNTO', 'direction', 'downto')


def test_shift_operator():
    operators = ['SLL', 'srl', 'SLa', 'sra', 'ROR', 'ROL']
    results = ['sll', 'srl', 'sla', 'sra', 'ror', 'rol']
    for (op, res) in zip(operators, results):
        check_visitor_return(op, 'shift_operator', res)


def test_relational_operator():
    operators = ['=', '/=', '<', '<=', '>', '>=']
    results = ['=', '/=', '<', '<=', '>', '>=']
    for (op, res) in zip(operators, results):
        check_visitor_return(op, 'relational_operator', res)


def test_logical_operator():
    operators = ['and', 'OR', 'nand', 'NoR', 'XOR', 'xnor']
    results = ['and', 'or', 'nand', 'nor', 'xor', 'xnor']
    for (op, res) in zip(operators, results):
        check_visitor_return(op, 'logical_operator', res)


def test_adding_operator():
    operators = ['+', '-', '&']
    results = ['+', '-', '&']
    for (op, res) in zip(operators, results):
        check_visitor_return(op, 'adding_operator', res)


def test_multiplying_operator():
    operators = ['*', '/', 'mod', 'REM']
    results = ['*', '/', 'mod', 'rem']
    for (op, res) in zip(operators, results):
        check_visitor_return(op, 'multiplying_operator', res)
