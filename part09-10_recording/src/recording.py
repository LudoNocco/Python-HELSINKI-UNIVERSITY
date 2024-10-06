class Recording:
    def __init__(self, length: int):
        self.__length = None
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value: int):
        if value < 0:
            raise ValueError("Length cannot be negative.")
        self.__length = value
