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

    def test_get_ports(self):
        entity = Entity('adder')
        rst_port = Port('rst', 'in', 'std_logic')
        entity.add_port(rst_port)
        clk_port = Port('clk', 'in', 'std_logic')
        entity.add_port(clk_port)
        list_of_ports = [port for port in entity.get_ports()]
        eq_(list_of_ports, entity._ports)
