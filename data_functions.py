import json

import display_functions


def read_in_data():
    """
    Function to read in data from data.json
    :return: dictionary of product data
    """
    import json
    fd = open("data.json", 'r')
    txt = fd.read()
    json_data = json.loads(txt)
    fd.close()
    return json_data


def read_in_recipes():
    """
    Function to read in data from data_recipe.json
    :return: Dictionary of recipe data
    """
    import json
    fd = open("data_recipe.json", 'r')
    txt = fd.read()
    json_data = json.loads(txt)
    fd.close()
    return json_data


def write_data(new_data):
    """
    Function to write data to data.json
    :param new_data: Dictionary of product data
    """
    js = json.dumps(new_data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()


def write_data_recipes(new_data):
    """
    Function to write data to data_recipe.json
    :param new_data: Dictionary of recipe data
    """
    js = json.dumps(new_data)
    fd = open("data-recipe.json", 'w')
    fd.write(js)
    fd.close()


def find_product_by_name(product_name, data):
    """
    Returns ID of product in dictionary by name
    :param product_name:  of product to find
    :param data: data dictionary
    :return: product id
    """
    p_id = -1
    for k, v in data.items():
        if str(v['name']) == product_name:
            p_id = k
    return p_id


def add_product():
    """
    Function for adding a complete new Product to the json file
    Ensures that no duplicate ID, however, name not primary key
    :return: True if success, else False
    """
    print("--- Inventory Management [Add Product] ---")
    data = read_in_data()
    temp_list = list(data.keys())
    p_id = int(temp_list[-1]) + 1
    if p_id not in data.keys():
        print("Enter Product Name: ")
        p_name = input().lower()
        print("Enter Product Type: ")
        p_type = input().lower()
        print("Enter Quantity: ")
        p_quantity = int(input())
        print("Enter Quantity units [l,ml,kg,g,count]")
        p_qunits = input().lower()
        print("Enter Date of Purchase in Form 31/12/2023")
        p_dop = input().lower()
        print("Enter Date of Expiry in Form 31/12/2023")
        p_doe = input().lower()
        print("Enter Number of Calories: ")
        p_cal = int(input())
        print("Enter Number of Protein: ")
        p_pro = int(input())
        print("Enter Number of Fat: ")
        p_fat = int(input())
        print("Enter Number of Carbohydrates: ")
        p_carb = int(input())
        print("Enter Number of Fiber: ")
        p_fiber = int(input())
        print("Enter Number of Sugar: ")
        p_sug = int(input())
        data[p_id] = {"name": p_name,
                      "type": p_type,
                      "quantity": p_quantity,
                      "quantity-units": p_qunits,
                      "date-purchase": p_dop,
                      "date-expire": p_doe,
                      "calories": p_cal,
                      "protein": p_pro,
                      "fat": p_fat,
                      "carbohydrates": p_carb,
                      "fiber": p_fiber,
                      "sugar": p_sug
                      }
    else:
        print("Product ID Error")
        print("------------------------------------------------")
        return False
    write_data(data)
    print("Product Successfully Added")
    print("------------------------------------------------")
    return True


def delete_product():
    """
    Function for deleting a Product from the JSON file
    Accepts product name, last found gets deleted
    :return: True if deleted, False otherwise
    """
    print("--- Inventory Management [Delete Product] ---")
    data = read_in_data()
    print("Enter Product Name for Deletion: ")
    p_name = input().lower()
    p_id = find_product_by_name(p_name, data)
    if p_id in data.keys():
        print("Product to be Deleted : " + str(data[p_id]))
        data.pop(p_id)
        print("Product Deleted Successful")
    else:
        print("Error Product not found")
        print("------------------------------------------------")
        return False
    write_data(data)
    print("------------------------------------------------")
    return True


def update_product():
    """
    Function to update product , identified by name
    :return: None
    """
    print("--- Inventory Management [Update Product] ---")
    data = read_in_data()
    print("Enter Product Name to Update: ")
    p_name = input().lower()
    p_id = find_product_by_name(p_name, data)
    if p_id == -1:
        print("Error Item could not be found")
        print("------------------------------------------------")
        return None
    print(data[p_id])
    print("Enter value to update: ")
    update_parameter = input()
    string_parameters = ['name', 'type', 'quantity-units', 'data-purchase', 'date-expire']
    int_parameters = ['calories', 'protein', 'fat', 'carbohydrates', 'fiber', 'sugar']
    if update_parameter in string_parameters:
        print(
            "Enter new value for: " + data[p_id]['name'] + " current value to change: " + data[p_id][update_parameter])
        new_value = input()
        data[p_id][update_parameter] = new_value
        write_data(data)

    elif update_parameter in int_parameters:
        print("Enter new value for: " + data[p_id]['name'] + " current value to change: " + str(
            data[p_id][update_parameter]))
        new_value = int(input())
        data[p_id][update_parameter] = new_value
        write_data(data)
    else:
        print("Error Unrecognised parameter")
        print("------------------------------------------------")
        return None
    print("Success: Product Updated: ")
    display_functions.display_specific_product_from_argument(data[p_id]['name'])
    print("------------------------------------------------")
    return None


def inventory_management_quantities():
    """
    Function used to update quantity of products
    :return: True if successful, False if error
    """
    print("--- Inventory Management [Update Quantities] ---")
    data = read_in_data()
    print("Please enter product name: ")
    p_name = input().lower()
    p_id = find_product_by_name(p_name, data)
    if p_id in data.keys():
        print(
            "Please enter the number by which you wish to adjust the quantity of " + str(data[p_id]['name']) + "i.e 1 "
                                                                                                               "or -1")
        print("Current quantity: " + str(data[p_id]['quantity']) + " " + str(data[p_id]['quantity-units']))
        adjustment = int(input())
        data[p_id]['quantity'] += adjustment
        write_data(data)
        print("Updated quantity: " + str(data[p_id]['quantity']) + " " + str(data[p_id]['quantity-units']))
    else:
        print("Error Product not found")
        print("------------------------------------------------")
        return False
    print("------------------------------------------------")
    return True


def data_names_to_list(data, in_stock):
    list_name = []
    for k, v in data.items():
        if in_stock:
            if v['quantity'] > 0:
                list_name.append(v['name'])
        else:
            list_name.append(v['name'])
    return list_name
