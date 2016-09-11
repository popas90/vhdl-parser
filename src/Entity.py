class Entity:

    def __init__(self, name):
        self.name = name
        self._ports = []
        self._generics = []

    def add_port(self, port):
        self._ports.append(port)
