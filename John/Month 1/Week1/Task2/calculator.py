while True:
    opera = input('enter the operator of your desired choice(+,-,/,*): ')
    num1 = float(input('enter the first number: '))
    num2 = float(input('enter the Second number: '))


    if opera == '+':
        print(f'{num1} + {num2} = {num1 + num2}')

    elif opera == '-':
        print(f'{num1} - {num2} = {num1 - num2}')

    elif opera == '/':
        if num2 == 0:
            print('!cannot divide using 0!')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')

    elif opera == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    
    choice = input('Do you wanna keep calculating?(y/n): ').lower()
    if choice == 'n':
        break
    
