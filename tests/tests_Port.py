from src.Port import Port
from nose.tools import eq_


class TestPort:

    def test_create(self):
        port = Port('rst', 'in', 'std_logic')
        eq_('rst', port.name)
        eq_('in', port.dir)
        eq_('std_logic', port.type)
