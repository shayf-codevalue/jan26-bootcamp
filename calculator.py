import sys
 # Usage: python calculator.py <operation> <num1> <num2>
 # Example: python calculator.py add 5 10
operation = sys.argv[1]
num1 = sys.argv[2]
num2 = sys.argv[3]
 
def calculate(op, a, b):
    a = int(a)
    b= int(b)
    if op == 'add':
        # TODO: RETURN HERE
        return a+b
    if op == 'subtract':
        # TODO: RETURN HERE
        return abs(a-b)
    if op == 'multiply':
        # TODO: RETURN HERE
        return a*b
    if op == 'divide':
        # TODO: RETURN HERE
        if b == 0:
            return 'Error: Division by zero and is not allowed.'
        return a/b
    return 'Unknown operation saas'
c=100
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
