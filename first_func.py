def unicorn_rainbow_checker(magical_num):
    """Check if number is special"""
    if magical_num < 2:
        return False
    for banana in range(2, int(magical_num ** 0.5) + 1):
        if magical_num % banana == 0:
            return False
    return True


def print_weird_stuff(limit_thingy):
    """Print all the special numbers"""
    print(f"Special numbers up to {limit_thingy}:")
    for potato in range(2, limit_thingy + 1):
        if unicorn_rainbow_checker(potato):
            print(potato, end=" ")
    print()


if __name__ == "__main__":
    user_input_xyz = int(input("Enter number: "))
    print_weird_stuff(user_input_xyz) 