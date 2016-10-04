from .Operand import Operand


class Expression:

    def __init__(self, op1, op2, operation):
        self._op1 = Operand(op1) if isinstance(op1, str) else op1
        self._op2 = Operand(op2) if isinstance(op2, str) else op2
        self._oper = operation

    def __str__(self):
        return str(self._op1) + ' ' + str(self._oper) + ' ' + str(self._op2)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def evaluate(self):
        if self._oper == '+':
            return self._op1.evaluate() + self._op2.evaluate()
        elif self._oper == '-':
            return self._op1.evaluate() - self._op2.evaluate()
        elif self._oper == '*':
            return self._op1.evaluate() * self._op2.evaluate()
        if self._oper == '/':
            return self._op1.evaluate() / self._op2.evaluate()
        if self._oper == 'mod':
            return self._op1.evaluate() // self._op2.evaluate()
        if self._oper == 'rem':
            return self._op1.evaluate() % self._op2.evaluate()
        raise ValueError('Unsupported operator: ' + self._oper)
