def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiply(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def divide(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    return round(c, 9)


def square(a):
    a = int(a)
    c = a ** 2
    return c


def sqrt(a):
    a = int(a)
    c = a ** 0.5
    return round(c, 9)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result
