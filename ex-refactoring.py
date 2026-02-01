# Order Processing System - Refactoring Exercise
# This code works but has several code smells. Can you identify and fix them?

def process(d, t, x):
    # d is data, t is type, x is extra
    result = []

    # Calculate discount
    if t == 1:
        if d["amount"] > 100:
            if d["member"] == True:
                disc = d["amount"] * 0.15
            else:
                disc = d["amount"] * 0.10
        else:
            if d["member"] == True:
                disc = d["amount"] * 0.05
            else:
                disc = 0
    elif t == 2:
        if d["amount"] > 100:
            if d["member"] == True:
                disc = d["amount"] * 0.20
            else:
                disc = d["amount"] * 0.15
        else:
            if d["member"] == True:
                disc = d["amount"] * 0.10
            else:
                disc = d["amount"] * 0.05

    final = d["amount"] - disc

    # Add tax
    final = final + (final * 0.08)

    # Format output
    print("Order processed")
    print("Original: " + str(d["amount"]))
    print("Discount: " + str(disc))
    print("Tax: " + str(final * 0.08))
    print("Final: " + str(final))

    # Log the order
    f = open("orders.log", "a")
    f.write("Order: " + str(d["amount"]) + ", Discount: " + str(disc) + ", Final: " + str(final) + "\n")
    f.close()

    return final


def validate_email(e):
    if e.find("@") != -1:
        if e.find(".") != -1:
            if len(e) > 5:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def calculate_shipping(w, z, e):
    # w = weight, z = zone, e = express
    cost = 0
    if z == 1:
        cost = w * 2.5
    if z == 2:
        cost = w * 3.5
    if z == 3:
        cost = w * 5.0
    if z == 4:
        cost = w * 7.5

    if e == True:
        cost = cost * 2

    # Add handling fee
    cost = cost + 3.99

    return cost


def get_user_info(id):
    # Unused variable
    temp = "temporary"
    debug_mode = True

    users = [
        {"id": 1, "name": "John", "email": "john@test.com", "age": 25},
        {"id": 2, "name": "Jane", "email": "jane@test.com", "age": 30},
        {"id": 3, "name": "Bob", "email": "bob@test.com", "age": 35},
    ]

    for i in range(0, len(users)):
        if users[i]["id"] == id:
            return users[i]

    return None


def format_price(p):
    return "$" + str(round(p, 2))


def format_price_euro(p):
    return str(round(p, 2)) + " EUR"


def format_price_gbp(p):
    return str(round(p, 2)) + " GBP"


# Main execution
if __name__ == "__main__":
    order_data = {"amount": 150, "member": True}
    total = process(order_data, 1, None)
    shipping = calculate_shipping(5, 2, True)
    print("Shipping: " + format_price(shipping))
