def print_options():
    print("--- Fridge Inventory System ---")
    while True:
        print(" [1] Display all available Products")
        print(" [2] Display specific Product")
        print(" [3] Display product database")
        print(" [4] Product inventory management")
        print(" [5] Display out of date Products")
        print(" [6] Display all possible recipes")
        print(" [7] Update quantities")
        print(" [8] Exit")

        user_input = int(input())
        if user_input == 1:
            display_all_available_products()
        elif user_input == 8:
            break


def display_all_available_products():
    print("TODO")
    #   TODO


if __name__ == '__main__':
    print_options()
