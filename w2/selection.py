# Input a positive number between 1 and 100 with error checking
def exercise_1():
    value = -1

    while value < 1 or value > 100:
        value = int(input('Please enter a valid number between 1 and 100\n'))

    if value % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")


# Input 3 numbers and an arithmetic operator
def exercise_2():
    total = 0

    for x in range(1, 4):
        value = int(input(f'[{x}] Enter value:\n'))
        operator = str(input(f'[{x}] Enter operator:\n'))

        match operator:
            case '+':
                old = total
                total += value
                print(f'{old} {operator} = {total}')
            case '-':
                old = total
                total -= value
                print(f'{old} {operator} = {total}')
            case '/':
                old = total
                total /= value
                print(f'{old} {operator} = {total}')
            case '*':
                old = total
                total *= value
                print(f'{old} {operator} = {total}')

    print(total)
