const args = process.argv.slice(2);
const operation = args[0];
const num1 = Number(args[1]);
const num2 = Number(args[2]);
 
function calculate(op, a, b) {
    if (op === 'add') {
        return a + b;
    }
    if (op === 'subtract') {
        return a - b;
    }
    if (op === 'multiply') {
        return a * b;
    }
    if (op === 'divide') {
        return a / b;
    }
    return 'Unknown operation';
}
 
const result = calculate(operation, num1, num2);
console.log('Result: ' + result);
