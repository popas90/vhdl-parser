class Expression:

    def __init__(self, operand1, operand2, operation):
        self._op1 = operand1
        self._op2 = operand2
        self._oper = operation

    def __str__(self):
        return str(self._op1) + ' ' + str(self._oper) + ' ' + str(self._op2)

    def eval(self):
        if self._oper == '+':
            return self._op1.eval() + self._op2.eval()
        elif self._oper == '-':
            return self._op1.eval() - self._op2.eval()
        elif self._oper == '*':
            return self._op1.eval() * self._op2.eval()
        if self._oper == '/':
            return self._op1.eval() / self._op2.eval()
        if self._oper == 'mod':
            return self._op1.eval() // self._op2.eval()
        if self._oper == 'rem':
            return self._op1.eval() % self._op2.eval()
        raise ValueError('Unsupported operator: ' + self._oper)
