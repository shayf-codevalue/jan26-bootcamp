# Order Processing System - Refactoring Exercise
# This code works but has several code smells. Can you identify and fix them?

def process(data, type, extra):
    amount = data["amount"]
    member = data["member"]
    disc = 0

    # Calculate discount
 if order_type == 1:
        if amount > 100:
            disc = amount * (0.15 if member else 0.10)
        else:
            disc = amount * 0.05 if member else 0

    elif order_type == 2:
        if amount > 100:
            disc = amount * (0.20 if member else 0.15)
        else:
            disc = amount * (0.10 if member else 0.05)

    else:
        raise ValueError("Unsupported order type")

    subtotal = amount - disc
    

    # Add tax
    tax=0.08*subtotal
    final=subtotal+tax

    # Format output
    print("Order processed")
    print("Original: " + str(amount))
    print("Discount: " + str(disc))
    print("Tax: " + str(tax))
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
