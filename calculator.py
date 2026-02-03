import sys
 
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
        return a/b
    return 'Unknown operation'
c=100
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
