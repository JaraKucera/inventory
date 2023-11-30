def read_in_data():
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    json_data = json.loads(txt)
    fd.close()
    return json_data


def data_to_table(search_item, quantity):
    data = read_in_data()
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
    data_to_table("all", True)
    return None


def display_specific_product():
    print("Please enter the identifier for which product(s) you want data for: ")
    search_value = str(input()).lower()
    data_to_table(search_value, False)
    return None


def display_product_database():
    data_to_table("all", False)
    return None


def inventory_management():
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
    return None


def display_possible_recipes():
    return None


def inventory_management_quantities():
    return None
