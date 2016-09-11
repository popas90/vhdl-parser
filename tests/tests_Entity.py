from src.Entity import Entity
from src.Port import Port
from nose.tools import eq_


class TestEntity:

    def test_create(self):
        entity = Entity('adder')
        eq_('adder', entity.name)
        eq_([], entity._generics)
        eq_([], entity._ports)

    def test_add_port(self):
        entity = Entity('adder')
        rst_port = Port('rst', 'in', 'std_logic')
        entity.add_port(rst_port)
        eq_([rst_port], entity._ports)
