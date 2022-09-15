class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1 * self.num2 

    def minus(self):
        return self.num1 * self.num2 
        
    def multiple(self):
        return self.num1 * self.num2 

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError: 
             print("0으로 나눌 수 없습니다.")

       
# 입력값을 받는다. 
while True: 
    try: 
        num1, num2 = map(int, input().split())
        break
    except ValueError:
        print("숫자만 입력 가능합니다")


calc = Calc(num1, num2)
calc.set_number(num1, num2)


print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값

