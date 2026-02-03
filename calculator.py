import sys
 
operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])
 
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
