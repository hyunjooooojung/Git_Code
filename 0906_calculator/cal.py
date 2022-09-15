def action(num1, num2, oper):
    if oper == '+':
        print(num1 + num2)

    elif oper == '-':
        print(num1 - num2)

    elif oper == '*':
        print(num1 * num2)

    elif oper == '/':
        print(num1 / num2)

    # 위 네가지의 연산자가 아닌것이 입력되면
    else:
        print('다시 입력해주세요')
