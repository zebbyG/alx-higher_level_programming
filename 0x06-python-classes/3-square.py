class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("")
