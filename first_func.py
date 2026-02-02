def print_weird_stuff(limit_thingy):
    """Print all the special numbers"""
    print(f"Special numbers up to {limit_thingy}:")
    for potato in range(2, limit_thingy + 1):
        is_special = True
        for banana in range(2, int(potato ** 0.5) + 1):
            if potato % banana == 0:
                is_special = False
                break
        if is_special:
            print(potato, end=" ")
    print()


if __name__ == "__main__":
    user_input_xyz = int(input("Enter number: "))
    print_weird_stuff(user_input_xyz) 