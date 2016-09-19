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
    literal = '22'
    visit_result = helpers.parse_string(literal,
                                        'abstract_literal')
    nose.tools.eq_('22', visit_result)
    literal = '22.33'
    visit_result = helpers.parse_string(literal,
                                        'abstract_literal')
    nose.tools.eq_('22.33', visit_result)
