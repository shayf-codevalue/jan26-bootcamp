# Order Processing System - Refactoring Exercise
# This code works but has several code smells. Can you identify and fix them?

# refactor the code to improve readability, maintainability, and efficiency:
# issues to address:
# 1. Poor naming conventions (process, d, t, x) (validate_email, e)  
# 2. Magic numbers in  order_processing function

import email


def order_processing(order_data, order_type):  # poor naming 
    # order_data is data, order_type is type, extra is extra deleted
    discount_amount_5 = 0.05
    discount_amount_10 = 0.10   
    discount_amount_15 = 0.15
    udiscount_amont_20 = 0.20    
    min_order_amount_for_discount = 100  # magic number

    # Calculate discount
    if order_type == 1:
        if order_data["amount"] > min_order_amount_for_discount: #(להוציא למתודה נפרדת)
            if order_data["member"]:
                discount = order_data["amount"] * discount_amount_15 
            else:
                discount = order_data["amount"] * discount_amount_10
            if order_data["member"]:
                discount = order_data["amount"] * discount_amount_5
            else:
                discount = 0
    elif order_type == 2:
        if order_data["amount"] > min_order_amount_for_discount:
            if order_data["member"]:
                discount = order_data["amount"] * udiscount_amont_20
            else:
                discount = order_data["amount"] * discount_amount_15
        else:
            if order_data["member"]:
                discount = order_data["amount"] * discount_amount_10
            else:
                discount = order_data["amount"] * discount_amount_5

    final_price = order_data["amount"] - discount

    # Add tax
    final_price =+ final_price * 0.08

    # Format output (להוציא למתודה נפרדת)
    print("Order processed")
    print("Original price: " + str(order_data["amount"]))
    print("Discount amount: " + str(discount))
    print("Tax amount: " + str(final_price * 0.08))
    print("Final price: " + str(final_price))

    # Log the order
    log_file = open("orders.log", "a")
    log_file.write("Order: " + str(order_data["amount"]) + ", Discount: " + str(discount) + ", Final: " + str(final_price) + "\n")
    log_file.close()

    return final_price

def user_email_valid(user_email):
    if  user_email.find("@") == -1:
        return False
    if user_email.find(".") == -1:
        return False
    if not len(user_email) <= 5:
        return False
    return True

# another version of user_email_valid function            
# def user_email_valid(user_email):
#     if  user_email.find("@") == -1 and  user_email.find(".") == -1 and not len(user_email) <= 5:
#         return False 
#     return True
                
        
    
        


def calculate_shipping_cost(weight, zone, express):
    # weight = weight, zone = zone, express = express
    shipping_cost = 0 
    # mapping zones to rates: map = {1: 2.5, 2: 3.5, 3: 5.0, 4: 7.5}, cost= weight * map[zone]
    if zone == 1: #(switch case better)
        shipping_cost = weight * 2.5
    if zone == 2:
        shipping_cost = weight * 3.5
    if zone == 3:
        shipping_cost = weight * 5.0
    if zone == 4:
        shipping_cost = weight * 7.5
    if express:
        shipping_cost = shipping_cost * 2

    # Add handling fee
    shipping_cost = shipping_cost + 3.99

    return shipping_cost


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


def format_price(p): #_default to usd format_price_USD
    return "$" + str(round(p, 2))


def format_price_euro(p):
    return str(round(p, 2)) + " EUR"


def format_price_gbp(p):
    return str(round(p, 2)) + " GBP"


# Main execution
if __name__ == "__main__":
    order_data = {"amount": 150, "member": True}
    total = order_processing(order_data, 1, None)
    shipping = calculate_shipping_cost(5, 2, True)
    print("Shipping: " + format_price(shipping))
