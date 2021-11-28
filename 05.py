class InputOutputString:
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input("Nhap : ")

    def printString(self):
        print('Upper: ' + self.s.upper())

strObj = InputOutputString()
strObj.getString()
strObj.printString()