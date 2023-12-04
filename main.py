import data_functions
import display_functions


def print_options():
    """
    Function which prints out all available options to the user
    """
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
            display_functions.display_all_available_products()
        elif user_input == 2:
            display_functions.display_specific_product()
        elif user_input == 3:
            display_functions.display_product_database()
        elif user_input == 4:
            display_functions.inventory_management()
        elif user_input == 5:
            display_functions.display_ood_products()
        elif user_input == 6:
            display_functions.display_possible_recipes()
        elif user_input == 7:
            data_functions.inventory_management_quantities()
        elif user_input == 8:
            break


if __name__ == '__main__':
    print_options()
