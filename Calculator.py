# Cli based Calculator of infinite values in python

def add(firstValue, *otherValues):  # Function for adding values.
    result = firstValue

    for i in otherValues:
        result = result + i

    print(result)


def sub(firstValue, *otherValues):  # Function for subtracting values.
    result = firstValue

    for i in otherValues:
        result = result - i

    print(result)


def multi(firstValue, *otherValues):  # Function for multiplication of values.
    result = firstValue

    for i in otherValues:
        result = result * i

    print(result)


def divd(firstValue, *otherValues):  # Function for dividing values.
    result = firstValue

    for i in otherValues:
        result = result - i

    print(result)


actn = input("Enter action you want to perform from following list "
             ":\nAddition\nSubtraction\nMultiplication\nDivide\n-> ")
values = [int(values) for values in input("Enter values: ").split()]
if actn == 'Addition' or actn == 'addition' or actn == 'ADD' or actn == 'add':
    print('Addition of values is: ', end="")
    add(*values)

elif actn == 'Subtraction' or actn == 'subtraction' or actn == 'SUB' or actn == 'sub':
    print('Subtraction of values is: ', end="")
    sub(*values)

elif actn == 'Multiplication' or actn == 'multiplication' or actn == 'MULTI' or actn == 'multi':
    print('Multiplication of values is: ', end="")
    multi(*values)

elif actn == 'Divide' or actn == 'divide' or actn == 'DIVIDE':
    print('Divide of values is: ', end="")
    divd(*values)

else:
    print('Wrong Input')
