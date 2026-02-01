// Order Processing System - Refactoring Exercise
// This code works but has several code smells. Can you identify and fix them?

const fs = require('fs');

function process(d, t, x) {
    // d is data, t is type, x is extra
    let result = [];
    let disc;

    // Calculate discount
    if (t === 1) {
        if (d.amount > 100) {
            if (d.member === true) {
                disc = d.amount * 0.15;
            } else {
                disc = d.amount * 0.10;
            }
        } else {
            if (d.member === true) {
                disc = d.amount * 0.05;
            } else {
                disc = 0;
            }
        }
    } else if (t === 2) {
        if (d.amount > 100) {
            if (d.member === true) {
                disc = d.amount * 0.20;
            } else {
                disc = d.amount * 0.15;
            }
        } else {
            if (d.member === true) {
                disc = d.amount * 0.10;
            } else {
                disc = d.amount * 0.05;
            }
        }
    }

    let final = d.amount - disc;

    // Add tax
    final = final + (final * 0.08);

    // Format output
    console.log("Order processed");
    console.log("Original: " + d.amount);
    console.log("Discount: " + disc);
    console.log("Tax: " + final * 0.08);
    console.log("Final: " + final);

    // Log the order
    fs.appendFileSync("orders.log", "Order: " + d.amount + ", Discount: " + disc + ", Final: " + final + "\n");

    return final;
}


function validateEmail(e) {
    if (e.indexOf("@") !== -1) {
        if (e.indexOf(".") !== -1) {
            if (e.length > 5) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}


function calculateShipping(w, z, e) {
    // w = weight, z = zone, e = express
    let cost = 0;
    if (z === 1) {
        cost = w * 2.5;
    }
    if (z === 2) {
        cost = w * 3.5;
    }
    if (z === 3) {
        cost = w * 5.0;
    }
    if (z === 4) {
        cost = w * 7.5;
    }

    if (e === true) {
        cost = cost * 2;
    }

    // Add handling fee
    cost = cost + 3.99;

    return cost;
}


function getUserInfo(id) {
    // Unused variable
    let temp = "temporary";
    let debugMode = true;

    const users = [
        {id: 1, name: "John", email: "john@test.com", age: 25},
        {id: 2, name: "Jane", email: "jane@test.com", age: 30},
        {id: 3, name: "Bob", email: "bob@test.com", age: 35},
    ];

    for (let i = 0; i < users.length; i++) {
        if (users[i].id === id) {
            return users[i];
        }
    }

    return null;
}


function formatPrice(p) {
    return "$" + p.toFixed(2);
}


function formatPriceEuro(p) {
    return p.toFixed(2) + " EUR";
}


function formatPriceGbp(p) {
    return p.toFixed(2) + " GBP";
}


// Main execution
const orderData = {amount: 150, member: true};
const total = process(orderData, 1, null);
const shipping = calculateShipping(5, 2, true);
console.log("Shipping: " + formatPrice(shipping));
