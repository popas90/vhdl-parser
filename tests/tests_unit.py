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
    visit_result = helpers.parse_string(generic,
                                        'interface_constant_declaration')
    nose.tools.eq_([Generic('kDepth', 'natural')], visit_result)


def test_abstract_literal():
    # ignoring BASE_LITERAL option for now
    literal = '22'
    visit_result = helpers.parse_string(literal, 'abstract_literal')
    nose.tools.eq_('22', visit_result)
    literal = '22.33'
    visit_result = helpers.parse_string(literal, 'abstract_literal')
    nose.tools.eq_('22.33', visit_result)


def test_numeric_literal():
    # ignoring PHYSICAL_LITERAL option for now
    literal = '52.3'
    visit_result = helpers.parse_string(literal, 'numeric_literal')
    nose.tools.eq_('52.3', visit_result)


def test_literal():
    literal = 'nULl'
    visit_result = helpers.parse_string(literal, 'literal')
    nose.tools.eq_('nULl', visit_result)
    literal = 'b1010'
    visit_result = helpers.parse_string(literal, 'literal')
    nose.tools.eq_('b1010', visit_result)
    literal = '1019'
    visit_result = helpers.parse_string(literal, 'literal')
    nose.tools.eq_('1019', visit_result)
    literal = 'h1A1F'
    visit_result = helpers.parse_string(literal, 'literal')
    nose.tools.eq_('h1A1F', visit_result)


def test_enumeration_literal():
    literal = 'this'
    visit_result = helpers.parse_string(literal, 'enumeration_literal')
    nose.tools.eq_('this', visit_result)
    literal = "'l'"
    visit_result = helpers.parse_string(literal, 'enumeration_literal')
    nose.tools.eq_("'l'", visit_result)
