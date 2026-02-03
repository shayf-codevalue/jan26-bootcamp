const args = process.argv.slice(2);
const operation = args[0];
const num1 = args[1];
const num2 = args[2];
 
function calculate(op, a, b) {
    if (op === 'add') {
        // TODO: RETURN HERE
    }
    if (op === 'subtract') {
        // TODO: RETURN HERE
    }
    if (op === 'multiply') {
        // TODO: RETURN HERE
    }
    if (op === 'divide') {
        // TODO: RETURN HERE
    }
    return 'Unknown operation';
}
 
const result = calculate(operation, num1, num2);
console.log('Result: ' + result);
