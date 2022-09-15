class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc = Calc(20, 10)
calc.set_number(20, 10)

print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값

