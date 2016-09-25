class Operand:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return 'Operand: ' + str(self)

    def __eq__(self, other):
        return self.evaluate() == other.evaluate()

    def __ne__(self, other):
        return not self == other

    def evaluate(self):
        try:
            return int(self._value)
        except ValueError:
            return float(self._value)
