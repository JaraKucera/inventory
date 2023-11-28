import json

sample_data = {
    1: {
        "name": "milk",
        "type": "dairy",
        "quantity": 1,
        "quantity-units": "l",
        "date-purchase": "01/01/2024",
        "date-expire": "08/01/2024",
        "calories": 0,
        "protein": 0,
        "fat": 0,
        "carbohydrates": 0,
        "fiber": 0,
        "sugar": 0
    },
    2: {
        "name": "plum",
        "type": "fruit",
        "quantity": 1,
        "quantity-units": "count",
        "date-purchase": "01/01/2024",
        "date-expire": "08/01/2024",
        "calories": 0,
        "protein": 0,
        "fat": 0,
        "carbohydrates": 0,
        "fiber": 0,
        "sugar": 0
    },
    3: {
        "name": "carrot",
        "type": "vegetable",
        "quantity": 1,
        "quantity-units": "count",
        "date-purchase": "01/01/2024",
        "date-expire": "08/01/2024",
        "calories": 0,
        "protein": 0,
        "fat": 0,
        "carbohydrates": 0,
        "fiber": 0,
        "sugar": 0
    }
}

js = json.dumps(sample_data)
fd = open("data.json", 'w')
fd.write(js)
fd.close()
