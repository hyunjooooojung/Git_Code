# cal.py를 불러와 action 함수를 실행시킨다.
import cal

num1 = int(input("첫번째 수를 입력하세요: "))
num2 = int(input("두번째 수를 입력하세요: "))
oper = input("연산자를 입력하세요(+, -, *, /) :")

# cal.py의 action함수를 불러와 실행시킴
cal.action(num1, num2, oper)

