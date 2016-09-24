from src.Entity import Entity
from src.Port import Port
from src.Generic import Generic
from nose.tools import eq_, ok_


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


class TestPort:

    def test_create(self):
        port = Port('rst', 'in', 'std_logic')
        eq_('rst', port.name)
        eq_('in', port.dir)
        eq_('std_logic', port.type)


class TestGeneric:

    def test_create(self):
        generic = Generic('kDepth', 'integer', '4')
        eq_('kDepth', generic.name)
        eq_('integer', generic.type)
        eq_('4', generic.init_value)

    def test_create_init_default(self):
        generic = Generic('kDepth', 'integer')
        eq_('kDepth', generic.name)
        eq_('integer', generic.type)
        eq_('', generic.init_value)

    def test_eq_ne(self):
        generic1 = Generic('kDepth', 'integer')
        generic2 = Generic('kDepth', 'integer', '')
        generic3 = Generic('kDepth', 'integer', '3')
        ok_(generic1 == generic2)
        ok_(generic1 != generic3)

    def test_repr(self):
        generic = Generic('kAll', 'integer', '3')
        eq_("Generic: {name: 'kAll', type: 'integer', init_value: '3'}",
            str(generic))
