import nose
import helpers
from src.Generic import Generic


def test_sanity():
    helpers.parse_file('./assets/empty.vhd')
    helpers.parse_string('', 'design_file')
    nose.tools.ok_(True)


def test_entity_declaration_empty():
    entity = 'entity Adder is end entity Adder;'
    visitor = helpers.parse_string(entity, 'design_file', True)
    nose.tools.eq_(visitor.entities[0].name, 'Adder')


def test_generic_declaration():
    generic = 'kDepth : natural'
    helpers.check_visitor_return(generic, 'interface_constant_declaration',
                                 [Generic('kDepth', 'natural')])


def test_abstract_literal():
    # ignoring BASE_LITERAL option for now
    helpers.check_visitor_return('22', 'abstract_literal', '22')
    helpers.check_visitor_return('22.33', 'abstract_literal', '22.33')


def test_numeric_literal():
    # ignoring PHYSICAL_LITERAL option for now
    helpers.check_visitor_return('52.3', 'numeric_literal', '52.3')


def test_literal():
    helpers.check_visitor_return('nULl', 'literal', 'nULl')
    helpers.check_visitor_return('b1010', 'literal', 'b1010')
    helpers.check_visitor_return('1019', 'literal', '1019')
    helpers.check_visitor_return('h1A1F', 'literal', 'h1A1F')


def test_enumeration_literal():
    helpers.check_visitor_return('this', 'enumeration_literal', 'this')
    helpers.check_visitor_return("'l'",  'enumeration_literal', "'l'")


def test_primary():
    helpers.check_visitor_return('b1011', 'primary', 'b1011')
