import json


def create_sample_inventory():
    sample_inventory_data = {
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

    js = json.dumps(sample_inventory_data)
    fd = open("data.json", 'w')
    fd.write(js)
    fd.close()


def create_sample_recipes():
    sample_recipe_data = {
        1: {
            "name": "Spaghetti Bologna",
            "total_calories": 600,
            "servings": 4,
            "preparation_time": 20,
            "cooking_time": 40,
            "difficulty": "medium",
            "cuisine_type": "Italian",
            "meal_type": "dinner",
            "dietary_information": ["meat", "gluten-free"],
            "allergens": ["wheat", "soy"],
            "required_ingredients": ["spaghetti", "ground beef", "tomato sauce", "onions", "garlic"],
            "instructions": "Cook spaghetti, brown beef with onions and garlic, add tomato sauce, and simmer until "
                            "flavors meld.",
            "nutritional_information": {
                "calories": 600,
                "protein": 25,
                "carbs": 60,
                "fats": 30
            },
            "equipment_needed": ["pot", "pan"],
            "tips_and_tricks": "Sprinkle Parmesan cheese before serving."
        },
        2: {
            "name": "Chicken Caesar Salad",
            "total_calories": 400,
            "servings": 2,
            "preparation_time": 15,
            "cooking_time": 0,
            "difficulty": "easy",
            "cuisine_type": "American",
            "meal_type": "lunch",
            "dietary_information": ["chicken", "gluten-free"],
            "allergens": ["egg", "fish"],
            "required_ingredients": ["chicken breast", "romaine lettuce", "croutons", "Caesar dressing"],
            "instructions": "Grill chicken, chop lettuce, mix with croutons, and toss with Caesar dressing.",
            "nutritional_information": {
                "calories": 400,
                "protein": 30,
                "carbs": 20,
                "fats": 22
            },
            "equipment_needed": ["grill pan", "bowl"],
            "tips_and_tricks": "Add cherry tomatoes for extra freshness."
        },
        3: {
            "name": "Vegetarian Stir-Fry",
            "total_calories": 350,
            "servings": 3,
            "preparation_time": 15,
            "cooking_time": 15,
            "difficulty": "easy",
            "cuisine_type": "Asian",
            "meal_type": "dinner",
            "dietary_information": ["vegetarian", "vegan"],
            "allergens": ["soy"],
            "required_ingredients": ["tofu", "broccoli", "carrots", "soy sauce"],
            "instructions": "Stir-fry tofu and vegetables, add soy sauce, and cook until veggies are tender.",
            "nutritional_information": {
                "calories": 350,
                "protein": 20,
                "carbs": 30,
                "fats": 18
            },
            "equipment_needed": ["wok", "pan"],
            "tips_and_tricks": "Use a variety of colorful vegetables for visual appeal."
        },
        4: {
            "name": "Oatmeal Breakfast Bowl",
            "total_calories": 300,
            "servings": 1,
            "preparation_time": 5,
            "cooking_time": 5,
            "difficulty": "easy",
            "cuisine_type": "Breakfast",
            "meal_type": "breakfast",
            "dietary_information": ["vegetarian", "gluten-free"],
            "allergens": ["nuts"],
            "required_ingredients": ["rolled oats", "milk", "banana", "nuts"],
            "instructions": "Cook oats with milk, top with sliced banana and nuts.",
            "nutritional_information": {
                "calories": 300,
                "protein": 10,
                "carbs": 50,
                "fats": 8
            },
            "equipment_needed": ["pot", "bowl"],
            "tips_and_tricks": "Drizzle honey for added sweetness."
        },
        5: {
            "name": "Mushroom Risotto",
            "total_calories": 700,
            "servings": 4,
            "preparation_time": 25,
            "cooking_time": 30,
            "difficulty": "medium",
            "cuisine_type": "Italian",
            "meal_type": "dinner",
            "dietary_information": ["vegetarian"],
            "allergens": ["wheat", "dairy"],
            "required_ingredients": ["Arborio rice", "mushrooms", "vegetable broth", "Parmesan cheese"],
            "instructions": "Sauté mushrooms, add rice, and gradually stir in vegetable broth until rice is creamy. "
                            "Finish with Parmesan.",
            "nutritional_information": {
                "calories": 700,
                "protein": 15,
                "carbs": 90,
                "fats": 28
            },
            "equipment_needed": ["pot", "pan"],
            "tips_and_tricks": "Stir constantly for the creamiest texture."
        }

    }
    js = json.dumps(sample_recipe_data)
    fd = open("data_recipe.json", 'w')
    fd.write(js)
    fd.close()


if __name__ == '__main__':
    create_sample_recipes()
