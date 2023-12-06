import time

import data_functions


def recipe_to_table(search_item, possible):
    data_rep = data_functions.read_in_recipes()
    from prettytable import PrettyTable
    table = PrettyTable(
        ["Name", "Total Calories", "Servings", "Preparation Time", "Cooking Time", "Difficulty", "Cuisine Type",
         "Allergens"])
    data = data_functions.read_in_data()
    in_fridge = data_functions.data_names_to_list(data, True)
    for k, v in data_rep.items():
        if possible:
            if search_item == "all":
                if set(v['required_ingredients']).issubset(set(in_fridge)):
                    table.add_row((v['name'].title(), str(v['total_calories']), str(v['servings']),
                                   str(v['preparation_time']),str(v['cooking_time']), v['difficulty'], v['cuisine_type'], v['allergens']))
            else:
                if v['name'] == search_item:
                    if set(v['required_ingredients']).issubset(set(in_fridge)):
                        table.add_row((v['name'].title(), str(v['total_calories']), str(v['servings']),
                                       str(v['preparation_time']), str(v['cooking_time']), v['difficulty'],
                                       v['cuisine_type'], v['allergens']))
        else:
            if search_item == "all":
                table.add_row((v['name'].title(), str(v['total_calories']), str(v['servings']),
                               str(v['preparation_time']), str(v['cooking_time']), v['difficulty'], v['cuisine_type'],
                               v['allergens']))
            else:
                if v['name'] == search_item:
                    table.add_row((v['name'].title(), str(v['total_calories']), str(v['servings']),
                                   str(v['preparation_time']), str(v['cooking_time']), v['difficulty'],
                                   v['cuisine_type'], v['allergens']))
    print(table, end="\n\n\n")


def data_to_table(search_item, quantity):
    """
    Function to turn dictionary product data into a table & display it :param search_item: if "all" all products are
    displayed in table, else only specified product :param quantity: if True, then quantity of items must be more
    than 0 to be printed out, else all products are printed
    """
    data = data_functions.read_in_data()
    from prettytable import PrettyTable
    table = PrettyTable(["Name", "Type", "Quantity", "Date of Purchase", "Date of Expire", "Calories", "Protein", "Fat",
                         "Carbohydrates", "Fiber", "Sugar"])
    for k, v in data.items():
        if quantity:
            if v['quantity'] > 0:
                if search_item == "all":
                    table.add_row(
                        [v['name'].title(), v['type'].title(), str(v['quantity']), v['date-purchase'], v['date-expire'],
                         str(v['calories']), str(v['protein']), str(v['fat']), str(v['carbohydrates']), str(v['fiber']),
                         str(v['sugar'])])
                elif search_item != "all" and search_item == v['name']:
                    table.add_row(
                        [v['name'].title(), v['type'].title(), str(v['quantity']), v['date-purchase'], v['date-expire'],
                         str(v['calories']), str(v['protein']), str(v['fat']), str(v['carbohydrates']), str(v['fiber']),
                         str(v['sugar'])])
        elif not quantity:
            if search_item == "all":
                table.add_row(
                    [v['name'].title(), v['type'].title(), str(v['quantity']), v['date-purchase'], v['date-expire'],
                     str(v['calories']), str(v['protein']), str(v['fat']), str(v['carbohydrates']), str(v['fiber']),
                     str(v['sugar'])])
            elif str(search_item) != "all" and str(search_item) == str(v['name']):
                table.add_row(
                    [v['name'].title(), v['type'].title(), str(v['quantity']), v['date-purchase'], v['date-expire'],
                     str(v['calories']), str(v['protein']), str(v['fat']), str(v['carbohydrates']), str(v['fiber']),
                     str(v['sugar'])])

    print(table, end="\n\n\n")


def display_all_available_products():
    """
    Function calls data_to_table with parameters of "all" and True
    :return: None
    """
    data_to_table("all", True)
    return None


def display_specific_product():
    """
    Function calls data_to_table that displays product based on name
    :return: None, prints out table to standard out
    """
    print("Please enter the identifier for which product(s) you want data for: ")
    search_value = str(input()).lower()
    data_to_table(search_value, False)
    return None


def display_specific_product_from_argument(product_name):
    """
    Function calls data_to_table that displays product based on name
    :return: None, prints out table to standard out
    """
    data_to_table(product_name, False)
    return None


def display_product_database():
    """
    Function calls data_to_table with all parameter and False
    :return:
    """
    data_to_table("all", False)
    return None


def inventory_management():
    """
    Prints out new menu for adding, deleting and adjusting products
    :return: None
    """
    import data_functions
    print("--- Inventory Management ---")
    while True:
        print(" [1] Add new Product")
        print(" [2] Delete existing Product")
        print(" [3] Adjust existing Product")
        print(" [4] Exit")

        user_choice = int(input())
        if user_choice == 1:
            data_functions.add_product()
        elif user_choice == 2:
            data_functions.delete_product()
        elif user_choice == 3:
            data_functions.update_product()
        elif user_choice == 4:
            break
    return None


def display_ood_products():
    from datetime import datetime
    current_date = time.strptime(str(datetime.today().strftime('%d/%m/%Y')), "%d/%m/%Y")
    data = data_functions.read_in_data()
    from prettytable import PrettyTable
    table = PrettyTable(["Name", "Type", "Quantity", "Date of Purchase", "Date of Expire", "Calories", "Protein", "Fat",
                         "Carbohydrates", "Fiber", "Sugar"])
    for k, v in data.items():
        if v['quantity'] > 0:
            expire_date = time.strptime(str(v['date-expire']), "%d/%m/%Y")
            if expire_date < current_date:
                table.add_row(
                    [v['name'].title(), v['type'].title(), str(v['quantity']), v['date-purchase'], v['date-expire'],
                     str(v['calories']), str(v['protein']), str(v['fat']), str(v['carbohydrates']), str(v['fiber']),
                     str(v['sugar'])])
    print(table, end="\n\n\n")
    return None


def display_possible_recipes():
    recipe_to_table("all", True)
    return None


def display_all_recipes():
    recipe_to_table("all", False)
    return None
