class Generic:

    def __init__(self, name, type, init_value=''):
        self.name = name
        self.type = type
        self.init_value = init_value

    def __repr__(self):
        # TODO rewrite this with format
        return 'Generic: {' + \
            "name: '" + str(self.name) + "', " + \
            "type: '" + str(self.type) + "', " + \
            "init_value: '" + str(self.init_value) + "'}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
