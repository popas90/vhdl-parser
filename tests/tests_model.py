from src.Entity import Entity
from src.Port import Port
from src.Generic import Generic
from src.Operand import Operand
from src.Expression import Expression
from nose.tools import eq_, ok_, raises


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


class TestOperand:

    def test_str(self):
        operand = Operand('-23')
        eq_('-23', str(operand))

    def test_repr(self):
        operand = Operand('-23')
        eq_('Operand: -23', repr(operand))

    def test_eq_ne(self):
        operand1 = Operand('+54')
        operand2 = Operand('54')
        operand3 = Operand('-54')
        ok_(operand1 == operand2)
        ok_(operand1 != operand3)

    def test_eval(self):
        operand = Operand('-23.02')
        eq_(-23.02, operand.evaluate())
        operand = Operand('25')
        eq_(25, operand.evaluate())

    @raises(ValueError)
    def test_eval_error(self):
        operand = Operand('-23.02a')
        eq_(-23.02, operand.evaluate())


class TestExpression:

    def test_str(self):
        op1 = Operand('-2')
        op2 = Operand('3')
        expr = Expression(op1, op2, '+')
        eq_('-2 + 3', str(expr))

    def test_eq_ne(self):
        op1 = Operand('54')
        op2 = Operand('+54')
        expr1 = Expression(op1, op2, '+')
        expr2 = Expression(op2, op1, '+')
        expr3 = Expression(op1, op2, '-')
        ok_(expr1 == expr2)
        ok_(expr1 != expr3)

    def test_eval(self):
        op1 = Operand('-2')
        op2 = Operand('+3')
        op3 = Operand('4')
        op4 = Operand('2')
        expr1 = Expression(op1, op2, '+')
        eq_(1, expr1.evaluate())
        expr2 = Expression(expr1, op2, '*')
        eq_(3, expr2.evaluate())
        expr3 = Expression(expr2, expr1, '-')
        eq_(2, expr3.evaluate())
        expr4 = Expression(op3, expr2, '/')
        eq_(float(4/3), expr4.evaluate())
        expr5 = Expression(op3, op4, 'mod')
        eq_(2, expr5.evaluate())
        expr6 = Expression(op3, op4, 'rem')
        eq_(0, expr6.evaluate())

    @raises(ValueError)
    def test_eval_error(self):
        op1 = Operand('-2')
        op2 = Operand('3')
        expr1 = Expression(op1, op2, 'and')
        eq_(1, expr1.evaluate())
