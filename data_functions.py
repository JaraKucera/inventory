import json


def add_product():
    """
    Function for adding a complete new Product to the json file
    Ensures that no duplicate ID, however, name not primary key
    :return: True if success, else False
    """
    print("--- Inventory Management [Add Product] ---")
    fd = open("data.json", 'r')
    ll = fd.read()
    data = json.loads(ll)
    fd.close()
    print(data)
    temp_list = list(data.keys())
    p_id = int(temp_list[-1]) + 1
    print(p_id)
    print(data.keys())
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
        return False
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()
    print("Product Successfully Added")
    return True


def delete_product():
    """
    Function for deleting a Product from the JSON file
    Accepts product name, last found gets deleted
    :return: True if deleted, False otherwise
    """
    print("--- Inventory Management [Delete Product] ---")
    fd = open("data.json", 'r')
    ll = fd.read()
    data = json.loads(ll)
    fd.close()
    print("Enter Product Name for Deletion: ")
    p_name = input().lower()
    p_id = 000000
    for k, v in data.items():
        if str(v['name']) == p_name:
            p_id = k
    if p_id in data.keys():
        print("Product to be Deleted : " + str(data[p_id]))
        data.pop(p_id)
        print("Product Deleted Successful")
    else:
        print("Error Product not found")
        return False
    js = json.dumps(data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()
    return True


def update_product():
    return None
