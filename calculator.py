import sys
 
operation = sys.argv[1]
num1 = sys.argv[2]
num2 = sys.argv[3]
 
def calculate(op, a, b):
    if op == 'add':
        # TODO: RETURN HERE
    if op == 'subtract':
        # TODO: RETURN HERE
    if op == 'multiply':
        # TODO: RETURN HERE
    if op == 'divide':
        # TODO: RETURN HERE
    return 'Unknown operation'
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
