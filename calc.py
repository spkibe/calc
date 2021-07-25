operation = input('operation type: ').lower()
num1 = input("First number: ")
num2 = input("First number: ")

try:
    num1, num2 = float(num1), float(num2)
    if operation == 'add':
        result = num1 + num2
        print(result)
    elif operation == 'subtract':
        result = num1 - num2
        print(result)
    elif operation == 'multiply':
        result = num1 * num2
        print(result)
    elif operation == 'divide':
        result = num1 / num2
        print(result)
    else:
        print('You didi choose the right operation')

except:
    #
    print("Impoper numbers or Operation")