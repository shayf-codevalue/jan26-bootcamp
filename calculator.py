import sys
 
operation = sys.argv[1]
num1 = sys.argv[2]
num2 = sys.argv[3]
 
def calculate(op, a, b):
    if op == 'add':
        return float(a) + float(b)
    if op == 'subtract':
        return float(a) - float(b)
    if op == 'multiply':
        return float(a) * float(b)
    if op == 'divide':
        if float(b) == 0:
            return 'Error: Division by zero'
        return float(a) / float(b)
    return 'Unknown operation'
 
result = calculate(operation, num1, num2)
print(f'Result: {result}')
