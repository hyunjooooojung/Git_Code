from curses.ascii import isdigit


count = 0
# 숫자를 5번 입력하면 프로그램이 종료된다.
while count < 5: 
    n = input()
    if n == 'exit':
        print("프로그램을 종료합니다.")
        break

    if n.isdigit() == True: 
        print(2 * int(n))
        count += 1
        
    elif n.isdigit() == False:
        print(f"입력한 문자는 {n} 입니다.")