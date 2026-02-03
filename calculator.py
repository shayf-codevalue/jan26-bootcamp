import sys
 
operation = sys.argv[1]
num1 = sys.argv[2]
num1 = int(num1)
num2 = sys.argv[3]
num2 = int(num2)
 
def calculate(op, a, b):
    if op == 'add':
        return a+b
    if op == 'subtract':
        return a-b
    if op == 'multiply':
        return a*b
    if op == 'divide' and b != 0:
        return a/b
    return 'Unknown operation'
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
