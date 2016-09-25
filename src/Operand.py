class Operand:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def eval(self):
        try:
            return int(self._value)
        except ValueError:
            return float(self._value)
