import sys
 
operation = sys.argv[1]
num1 = sys.argv[2]
num2 = sys.argv[3]
 
def calculate(op, a, b):
    a=int(a)
    b=int(b)
    op = op.lower()
    if op == 'add':
        return a+b
    if op == 'subtract':
        return a-b
    if op == 'multiply':
        return a*b
    if op == 'divide':
        return a/b
    return 'Unknown operation'
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
