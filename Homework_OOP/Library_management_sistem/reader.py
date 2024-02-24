class Reader:

    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def add_reader(self, name, id_):
        reader = Reader(name, id_)
        self.reader.append(reader)
        return f"Added Reader: {name}"
